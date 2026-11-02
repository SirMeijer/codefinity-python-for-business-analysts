import pandas as pd

def automate_regional_analysis(north_sales, south_sales):
    # Write your code here
    def clean_sales_data(sales):
        cleaned = []
        for item in sales:
            if not isinstance(item, dict):
                continue
            product = item.get("product")
            sales_value = item.get("sales")
            if not product or sales_value is None:
                continue
            try:
                sales_float = float(sales_value)
            except (ValueError, TypeError):
                continue
            cleaned.append({"product": product.strip(), "sales": sales_float})
        return cleaned

    def summarize_products(sales):
        summary = {}
        for item in sales:
            product = item["product"]
            summary[product] = summary.get(product, 0) + item["sales"]
        return summary

    def generate_report(region, summary):
        lines = [f"Sales Report for {region} Region:"]
        if not summary:
            lines.append("No valid sales data.")
        else:
            for product, total in sorted(summary.items()):
                lines.append(f"{product}: {total:.2f}")
        return "\n".join(lines)

    regions = {"North": north_sales, "South": south_sales}
    reports = {}
    for region, sales in regions.items():
        cleaned = clean_sales_data(sales)
        summary = summarize_products(cleaned)
        reports[region] = generate_report(region, summary)            
    return reports

north_sales = [
    {"product": "Widget", "sales": "100.5"},
    {"product": "Gadget", "sales": 85},
    {"product": "Widget", "sales": "invalid"},
    {"product": "Gizmo", "sales": 50},
    {"product": None, "sales": 30},
    "not a dict",
    {"product": "Widget", "sales": 25.0}
]

south_sales = [
    {"product": "Widget", "sales": "75"},
    {"product": "Gadget", "sales": 95.5},
    {"product": "", "sales": 20},
    {"product": "Gizmo", "sales": None},
    {"product": "Gadget", "sales": "10"},
    {"product": "Widget", "sales": 40}
]

result = automate_regional_analysis(north_sales, south_sales)
north_report = result["North"]
south_report = result["South"]
print(north_report)
print(south_report)
