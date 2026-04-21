import json
from collections import Counter, defaultdict

# Load the data
with open(r'c:\Users\1\Desktop\项目测试\pcindia\tgstat_export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['items']
print(f"Total items in dataset: {len(items)}\n")

# 1. All unique category values
categories = set(item['category'] for item in items if 'category' in item)
print("=" * 60)
print("1. ALL UNIQUE CATEGORY VALUES")
print("=" * 60)
for cat in sorted(categories):
    print(f"  - {cat}")
print(f"\nTotal unique categories: {len(categories)}\n")

# 2. All unique categoryCode values
category_codes = set(item['categoryCode'] for item in items if 'categoryCode' in item)
print("=" * 60)
print("2. ALL UNIQUE CATEGORY CODE VALUES")
print("=" * 60)
for code in sorted(category_codes):
    print(f"  - {code}")
print(f"\nTotal unique category codes: {len(category_codes)}\n")

# 3. Count items per category
print("=" * 60)
print("3. ITEM COUNT PER CATEGORY")
print("=" * 60)
category_counts = Counter(item['category'] for item in items if 'category' in item)
for cat, count in category_counts.most_common():
    print(f"  {cat}: {count:,} items")
print()

# 4. Top 20 channels by sum (subscriber count) for each major category
print("=" * 60)
print("4. TOP 20 CHANNELS BY SUBSCRIBERS FOR EACH MAJOR CATEGORY")
print("=" * 60)

# Group items by category
items_by_category = defaultdict(list)
for item in items:
    if 'category' in item:
        items_by_category[item['category']].append(item)

for category in sorted(items_by_category.keys()):
    category_items = items_by_category[category]
    # Sort by sum (subscriber count) descending
    sorted_items = sorted(category_items, key=lambda x: x.get('sum', 0), reverse=True)
    top_20 = sorted_items[:20]
    
    print(f"\n--- {category} ({len(category_items):,} total items) ---")
    for i, item in enumerate(top_20, 1):
        subscribers = item.get('sum', 0)
        title = item.get('title', 'N/A')
        item_type = item.get('type', 'N/A')
        country = item.get('country', 'N/A')
        print(f"  {i:2}. {title[:50]:<50} | {subscribers:>12,} subs | {item_type:<10} | {country}")

# 5. Unique type values
print("\n" + "=" * 60)
print("5. UNIQUE TYPE VALUES")
print("=" * 60)
types = Counter(item['type'] for item in items if 'type' in item)
for t, count in types.most_common():
    print(f"  {t}: {count:,} items")
print()

# 6. Other interesting metadata patterns
print("=" * 60)
print("6. OTHER INTERESTING METADATA PATTERNS")
print("=" * 60)

# Country distribution
print("\n--- Country Distribution (Top 20) ---")
countries = Counter(item['country'] for item in items if 'country' in item)
for country, count in countries.most_common(20):
    print(f"  {country}: {count:,} items")

# Last post activity
print("\n--- Last Post Activity Patterns ---")
last_post_patterns = Counter(item['lastPostAgo'] for item in items if 'lastPostAgo' in item)
for pattern, count in last_post_patterns.most_common(15):
    print(f"  {pattern}: {count:,} items")

# Description stats
print("\n--- Description Stats ---")
with_desc = sum(1 for item in items if item.get('description'))
without_desc = sum(1 for item in items if not item.get('description'))
print(f"  Items with description: {with_desc:,} ({with_desc/len(items)*100:.1f}%)")
print(f"  Items without description: {without_desc:,} ({without_desc/len(items)*100:.1f}%)")

# Subscriber statistics
print("\n--- Subscriber Statistics ---")
sums = [item['sum'] for item in items if 'sum' in item]
print(f"  Total subscribers across all channels: {sum(sumS):,}")
print(f"  Average subscribers: {sum(sums)//len(sums):,}")
print(f"  Max subscribers: {max(sums):,}")
print(f"  Min subscribers: {min(sums):,}")

# Category to categoryCode mapping
print("\n--- Category to CategoryCode Mapping ---")
cat_code_map = {}
for item in items:
    cat = item.get('category')
    code = item.get('categoryCode')
    if cat and code:
        cat_code_map[cat] = code
for cat in sorted(cat_code_map.keys()):
    print(f"  {cat} -> {cat_code_map[cat]}")

# CrawledAt date range
print("\n--- Crawl Date Range ---")
crawl_dates = set(item['crawledAt'].split()[0] for item in items if 'crawledAt' in item)
for date in sorted(crawl_dates):
    print(f"  {date}")
