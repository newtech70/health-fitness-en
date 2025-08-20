import os
import datetime
import requests
import time

# Variables
affiliate_id = os.environ['AFFILIATE_ID']
unsplash_key = os.environ['UNSPLASH_ACCESS_KEY']

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

# Fetch images Unsplash
def get_unsplash_images(niche, num=5):
    queries = {
        'health-fitness': ['workout', 'yoga', 'nutrition', 'gym', 'wellness'],
        'personal-finance': ['money', 'budget', 'investment', 'savings', 'finance'],
        'tech-ai': ['technology', 'artificial intelligence', 'coding', 'gadgets', 'innovation'],
        'food-recipes': ['cooking', 'recipe', 'food', 'kitchen', 'dessert'],
        'pets': ['dog', 'cat', 'pet care', 'animals', 'puppy']
    }
    urls = []
    for i in range(num):
        query = queries[niche][i % len(queries[niche])]
        try:
            response = requests.get(
                f'https://api.unsplash.com/search/photos?query={query}&per_page=1&client_id={unsplash_key}',
                timeout=5
            )
            if response.status_code == 200 and response.json()['results']:
                urls.append(response.json()['results'][0]['urls']['small'])
            else:
                urls.append('https://via.placeholder.com/300x200')
        except:
            urls.append('https://via.placeholder.com/300x200')
        time.sleep(1)
    return urls

# Contenu statique
content = '''
<h2 id="intro">Introduction</h2>
<p>Welcome to our <strong>{niche}</strong> guide in {lang}! Whether you're a beginner or an expert, this article provides practical tips to excel in {niche}. From building sustainable habits to using the best tools available on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>, we’ve got you covered with actionable strategies to achieve your goals in a healthy and effective way. Let’s dive into the essentials of {niche} and how you can start improving today!</p>

<h2 id="tips">Top {niche.capitalize()} Tips</h2>
<p>Here are some foundational tips to kickstart your {niche} journey:</p>
<ul>
    <li><strong>Start Small</strong>: Begin with manageable steps, like a 10-minute daily workout or setting a weekly fitness goal. Small wins build momentum.</li>
    <li><strong>Use Quality Equipment</strong>: Invest in reliable tools like dumbbells, yoga mats, or fitness trackers from <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a> to enhance your routine.</li>
    <li><strong>Stay Consistent</strong>: Consistency is key. Schedule your workouts or wellness activities at the same time each day to form habits.</li>
    <li><strong>Plan Your Nutrition</strong>: A balanced diet fuels your body. Explore meal prep kits or supplements on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
    <li><strong>Hydrate Regularly</strong>: Drink at least 8 glasses of water daily to support energy and recovery.</li>
</ul>

<h2>Advanced Strategies for {niche.capitalize()}</h2>
<p>Once you’ve mastered the basics, take your {niche} efforts to the next level with these strategies:</p>
<ul>
    <li><strong>Track Your Progress</strong>: Use apps or fitness journals to monitor your workouts, diet, or goals. Check out fitness trackers on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
    <li><strong>Incorporate Variety</strong>: Mix cardio, strength training, and flexibility exercises to avoid plateaus and keep things fun.</li>
    <li><strong>Learn from Experts</strong>: Follow top {niche} blogs, watch tutorials, or read books available on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
    <li><strong>Optimize Recovery</strong>: Prioritize sleep and active recovery days to prevent burnout and injuries.</li>
    <li><strong>Set SMART Goals</strong>: Specific, Measurable, Achievable, Relevant, Time-bound goals keep you focused.</li>
</ul>

<h2>Common Mistakes to Avoid</h2>
<p>Avoid these pitfalls to ensure long-term success in {niche}:</p>
<ul>
    <li><strong>Overtraining</strong>: Pushing too hard without rest leads to burnout or injuries. Balance is crucial.</li>
    <li><strong>Ignoring Nutrition</strong>: Exercise alone isn’t enough; pair it with a balanced diet.</li>
    <li><strong>Skipping Warm-Ups</strong>: Always warm up to prevent injuries and improve performance.</li>
    <li><strong>Relying on Fads</strong>: Avoid trendy diets or workouts; stick to proven methods.</li>
    <li><strong>Not Tracking</strong>: Without monitoring, it’s hard to know what works. Use tools from <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
</ul>

<h2>Recommended Tools for Success</h2>
<p>Here are some must-have tools to enhance your {niche} experience:</p>
<ul>
    <li><strong>Fitness Trackers</strong>: Monitor steps, heart rate, and calories with devices from <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
    <li><strong>Home Gym Equipment</strong>: Dumbbells, resistance bands, or yoga mats for versatile workouts.</li>
    <li><strong>Nutrition Guides</strong>: Books or meal planners to stay on track with your diet.</li>
    <li><strong>Water Bottles</strong>: Stay hydrated with reusable bottles from <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a>.</li>
</ul>
<p>These tools are affordable, effective, and available on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a> to support your journey.</p>

<h2 id="conclusion">Conclusion</h2>
<p>Mastering <strong>{niche}</strong> is about starting small, staying consistent, and using the right tools. Whether you’re focusing on workouts, nutrition, or recovery, these tips provide a solid foundation for success. Explore high-quality resources on <a href="https://amazon.com/product?tag={affiliate_id}">Amazon</a> to take your {niche} game to the next level. Stay tuned for more expert advice, and start implementing these strategies today to see real results!</p>
'''

# Images
images = get_unsplash_images(niche)

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
    <meta name="description" content="Best {niche} tips in {lang}">
    <meta name="keywords" content="{niche}, tips, guide, {lang}">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="../styles.css" rel="stylesheet">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CODE}" crossorigin="anonymous"></script>
    <script type="application/ld+json">
    {{ "@type": "BlogPosting", "headline": "Article {num}", "image": "{images[0]}", "datePublished": "{date}", "author": {{ "@type": "Person", "name": "NewTech70" }} }}
    </script>
</head>
<body style="font-family: 'Roboto', sans-serif;">
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: {niche_colors[niche]}; padding: 1rem;">
        <div class="container">
            <a class="navbar-brand text-white" href="/">{niche.capitalize()} Tips</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="/articles">Articles</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="/about">About</a></li>
                </ul>
                <form class="d-flex ms-3">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-light" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
    <div class="container mt-4" style="padding: 2rem;">
        <h1>Article {num} : {niche.capitalize()} Tips</h1>
        <div class="toc mb-3">
            <h4>Table of Contents</h4>
            <ul>
                <li><a href="#intro">Introduction</a></li>
                <li><a href="#tips">Tips</a></li>
                <li><a href="#conclusion">Conclusion</a></li>
            </ul>
        </div>
        <img src="{images[0]}" class="img-fluid mb-3" alt="{niche} article {num} featured" loading="lazy">
        {content}
        <img src="{images[1]}" class="img-fluid mb-3" alt="{niche} in-content 1" loading="lazy">
        <img src="{images[2]}" class="img-fluid mb-3" alt="{niche} in-content 2" loading="lazy">
        <ins class="adsbygoogle" style="display:block; margin: 2rem 0;" data-ad-client="{ADSENSE_CODE}" data-ad-slot="0987654321" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
        <img src="{images[3]}" class="img-fluid mb-3" alt="{niche} in-content 3" loading="lazy">
        <img src="{images[4]}" class="img-fluid mb-3" alt="{niche} in-content 4" loading="lazy">
        <div class="related mt-4">
            <h3>Related Articles</h3>
            <ul>
                <li><a href="/articles/2025-08-20-1.html">Article 1</a></li>
                <li><a href="/articles/2025-08-20-2.html">Article 2</a></li>
            </ul>
        </div>
    </div>
    <footer class="bg-dark text-white text-center py-3 mt-4">
        <p>&copy; 2025 {niche.capitalize()} Tips. All rights reserved.</p>
        <a href="/privacy" class="text-white">Privacy Policy</a> | <a href="/sitemap" class="text-white">Sitemap</a>
        <div class="social-icons">
            <a href="#" class="text-white me-2">Facebook</a>
            <a href="#" class="text-white me-2">Twitter</a>
            <a href="#" class="text-white">Instagram</a>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>''')
