import os
import datetime
import google.generativeai as genai

# Configurer Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')
affiliate_id = os.environ['AFFILIATE_ID']

# Extraire niche et langue
repo_name = os.environ.get('GITHUB_REPOSITORY', 'newtech70/health-fitness-en').split('/')[-1]
niche, lang = repo_name.split('-')

# Couleurs niches
niche_colors = {
    'health-fitness': '#28a745',
    'personal-finance': '#007bff',
    'tech-ai': '#6f42c1',
    'food-recipes': '#fd7e14',
    'pets': '#dc3545'
}

# Générer article
prompt = f"Article SEO quotidien 1500 mots pour {niche} en {lang}, keywords, affiliates https://amazon.com/product?tag={affiliate_id}"
response = model.generate_content(prompt)
content = response.text

# Sauvegarder article
date = datetime.date.today().strftime("%Y-%m-%d")
num = len([f for f in os.listdir('articles') if f.endswith('.html')]) + 1
os.makedirs('articles', exist_ok=True)
with open(f'articles/{date}-{num}.html', 'w', encoding='utf-8') as f:
    f.write(f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Article {num} {niche.capitalize()}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="../styles.css" rel="stylesheet">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-placeholder" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: {niche_colors.get(niche, '#28a745')};">
        <div class="container">
            <a class="navbar-brand text-white" href="/">{niche.capitalize()} Tips</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="/articles">Articles</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="/about">About</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-4">
        <h1>Article {num} for {niche.capitalize()}</h1>
        <img src="https://via.placeholder.com/300x200" class="img-fluid mb-3" alt="{niche}">
        {content}
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-placeholder"
             data-ad-slot="0987654321"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    <footer class="bg-dark text-white text-center py-3 mt-4">
        <p>&copy; 2025 {niche.capitalize()} Tips. All rights reserved.</p>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>''')
