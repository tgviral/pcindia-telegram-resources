import json
import sys
from collections import Counter, defaultdict

# Fix UTF-8 output for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Load the JSON data
with open('c:\\Users\\1\\Desktop\\项目测试\\pcindia\\tgstat_export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['items']
print(f"Total items: {len(items)}\n")

# 1. All unique category values
categories = set(item.get('category', 'N/A') for item in items)
print("=" * 60)
print("1. ALL UNIQUE CATEGORY VALUES:")
print("=" * 60)
for cat in sorted(categories):
    print(f"  - {cat}")

# 2. All unique categoryCode values
category_codes = set(item.get('categoryCode', 'N/A') for item in items)
print("\n" + "=" * 60)
print("2. ALL UNIQUE CATEGORY CODE VALUES:")
print("=" * 60)
for code in sorted(category_codes):
    print(f"  - {code}")

# 3. Count items per category
category_counts = Counter(item.get('category', 'N/A') for item in items)
print("\n" + "=" * 60)
print("3. COUNT OF ITEMS PER CATEGORY:")
print("=" * 60)
for cat, count in category_counts.most_common():
    print(f"  {cat}: {count}")

# 4. Top 20 channels by "sum" for each major category
print("\n" + "=" * 60)
print("4. TOP 20 CHANNELS BY SUBSCRIBERS (sum) PER MAJOR CATEGORY:")
print("=" * 60)

# Group items by category
by_category = defaultdict(list)
for item in items:
    cat = item.get('category', 'N/A')
    by_category[cat].append(item)

for cat in sorted(by_category.keys(), key=lambda x: len(by_category[x]), reverse=True):
    channels = by_category[cat]
    # Sort by sum descending
    sorted_channels = sorted(channels, key=lambda x: x.get('sum', 0), reverse=True)
    top_20 = sorted_channels[:20]
    
    print(f"\n--- {cat} ({len(channels)} total) ---")
    for i, ch in enumerate(top_20, 1):
        print(f"  {i:2}. {ch.get('title', 'N/A')[:40]:<40} | {ch.get('sum', 0):>10,} | @{ch.get('username', 'N/A')}")

# 5. Unique type values
types = set(item.get('type', 'N/A') for item in items)
type_counts = Counter(item.get('type', 'N/A') for item in items)
print("\n" + "=" * 60)
print("5. UNIQUE TYPE VALUES & COUNTS:")
print("=" * 60)
for t, count in type_counts.most_common():
    print(f"  {t}: {count}")

# 6. Other interesting metadata patterns
print("\n" + "=" * 60)
print("6. OTHER INTERESTING METADATA PATTERNS:")
print("=" * 60)

# Country distribution
countries = Counter(item.get('country', 'N/A') for item in items)
print("\n--- Country Distribution ---")
for country, count in countries.most_common(15):
    print(f"  {country}: {count}")

# Description patterns
has_description = sum(1 for item in items if item.get('description'))
no_description = len(items) - has_description
print(f"\n--- Description Stats ---")
print(f"  Channels with descriptions: {has_description} ({has_description/len(items)*100:.1f}%)")
print(f"  Channels without descriptions: {no_description} ({no_description/len(items)*100:.1f}%)")

# lastPostAgo patterns
post_ages = Counter(item.get('lastPostAgo', 'N/A') for item in items)
print(f"\n--- Posting Activity (lastPostAgo patterns) ---")
for age, count in post_ages.most_common(10):
    print(f"  {age}: {count}")

# Average subscribers by type
print(f"\n--- Average Subscribers by Type ---")
type_sums = defaultdict(list)
for item in items:
    t = item.get('type', 'N/A')
    s = item.get('sum', 0)
    type_sums[t].append(s)
for t, sums in type_sums.items():
    avg = sum(sums) / len(sums)
    print(f"  {t}: {avg:,.0f} avg subscribers ({len(sums)} channels)")

# Total subscribers
total_subs = sum(item.get('sum', 0) for item in items)
print(f"\n--- Total Subscribers Across All Channels: {total_subs:,} ---")

# Top overall channels
sorted_all = sorted(items, key=lambda x: x.get('sum', 0), reverse=True)
print(f"\n--- TOP 30 OVERALL CHANNELS BY SUBSCRIBERS ---")
for i, ch in enumerate(sorted_all[:30], 1):
    print(f"  {i:2}. {ch.get('title', 'N/A')[:45]:<45} | {ch.get('sum', 0):>10,} | {ch.get('category', 'N/A')[:20]}")

# Category-Code mapping
print(f"\n--- Category to CategoryCode Mapping ---")
cat_code_map = {}
for item in items:
    cat = item.get('category', 'N/A')
    code = item.get('categoryCode', 'N/A')
    if cat not in cat_code_map:
        cat_code_map[cat] = code
for cat, code in sorted(cat_code_map.items()):
    print(f"  {cat} -> {code}")
