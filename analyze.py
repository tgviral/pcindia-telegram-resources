import json
from collections import Counter

# Load JSON
with open(r'c:\Users\1\Desktop\项目测试\pcindia\tgstat_export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['items']

print("=" * 60)
print("TGSTAT EXPORT JSON ANALYSIS FOR SEO ARTICLE PLANNING")
print("=" * 60)

# 1. Basic stats
print(f"\n1. TOTAL ITEMS: {len(items):,}")

# 2. Unique type values
types = list(set(item['type'] for item in items))
print(f"\n2. UNIQUE TYPE VALUES ({len(types)}):")
for t in sorted(types):
    count = sum(1 for item in items if item['type'] == t)
    print(f"   - {t}: {count:,} items")

# 3. Unique category values
categories = list(set(item.get('category', '') for item in items))
print(f"\n3. UNIQUE CATEGORY VALUES ({len(categories)}):")
for c in sorted(categories):
    count = sum(1 for item in items if item.get('category') == c)
    print(f"   - {c}: {count:,} items")

# 4. Unique categoryCode values
category_codes = list(set(item.get('categoryCode', '') for item in items))
print(f"\n4. UNIQUE CATEGORY CODE VALUES ({len(category_codes)}):")
for cc in sorted(category_codes):
    count = sum(1 for item in items if item.get('categoryCode') == cc)
    print(f"   - {cc}: {count:,} items")

# 5. Count per category (detailed)
print("\n5. COUNT PER CATEGORY (DETAILED):")
category_counts = Counter(item.get('category', '') for item in items)
for cat, count in category_counts.most_common():
    print(f"   - {cat}: {count:,}")

# 6. Count per categoryCode
print("\n6. COUNT PER CATEGORY CODE:")
categorycode_counts = Counter(item.get('categoryCode', '') for item in items)
for cc, count in categorycode_counts.most_common():
    print(f"   - {cc}: {count:,}")

# 7. Countries present
print("\n7. COUNTRIES PRESENT:")
countries = Counter(item.get('country', '') for item in items)
for country, count in countries.most_common(20):
    print(f"   - {country}: {count:,}")

# 8. Top 20 overall by sum
print("\n8. TOP 20 CHANNELS BY SUBSCRIBER COUNT (OVERALL):")
top20 = sorted(items, key=lambda x: x.get('sum', 0), reverse=True)[:20]
for i, item in enumerate(top20, 1):
    print(f"   {i:2}. {item['title'][:40]:<42} | {item.get('sum', 0):>12,} | {item.get('category', 'N/A')[:25]}")

# 9. Top channels per major category
print("\n9. TOP 20 CHANNELS BY CATEGORY:")
for cat in ['Business and services', 'Education', 'Entertainment', 'News', 'Sports', 'Politics', 'Travel', 'Technology']:
    print(f"\n   --- {cat} ---")
    cat_items = [item for item in items if item.get('category') == cat]
    if cat_items:
        top_cat = sorted(cat_items, key=lambda x: x.get('sum', 0), reverse=True)[:10]
        for i, item in enumerate(top_cat, 1):
            print(f"     {i:2}. {item['title'][:50]:<52} | {item.get('sum', 0):>12,}")

# 10. Category -> categoryCode mapping
print("\n10. CATEGORY TO CATEGORY CODE MAPPING:")
cc_mapping = {}
for item in items:
    key = (item.get('category'), item.get('categoryCode'))
    if key not in cc_mapping:
        cc_mapping[key] = 1
for (cat, cc), _ in sorted(cc_mapping.items()):
    print(f"   - {cat} => {cc}")

# 11. Other patterns
print("\n11. OTHER METADATA PATTERNS:")
print(f"   - Items with description: {sum(1 for item in items if item.get('description')):,}")
print(f"   - Items without description: {sum(1 for item in items if not item.get('description')):,}")
print(f"   - Items with username: {sum(1 for item in items if item.get('username')):,}")
print(f"   - Items without username: {sum(1 for item in items if not item.get('username')):,}")

# 12. Sum statistics
sums = [item.get('sum', 0) for item in items]
print(f"\n12. SUBSCRIBER COUNT STATISTICS:")
print(f"   - Total subscribers (sum of all): {sum(sums):,}")
print(f"   - Average subscribers: {sum(sums)//len(sums):,}")
print(f"   - Max subscribers: {max(sums):,}")
print(f"   - Min subscribers: {min(sums):,}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)
