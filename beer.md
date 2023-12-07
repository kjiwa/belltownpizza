---
layout: page
title: Beer
cover-img: /assets/img/btp-cover-menu.jpg
---

## Drafts

{% assign x = site.data.beer | where: "Category", "Drafts" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
* Rotating Cider
* Rotating IPA
* Rotating Pale Ale
* Rotating Pilsner
* Rotating Seasonal Draft

## Bottled/Canned Beer, Cider, and Seltzers

{% assign categories = "Domestics,Imports,Locals,Ciders,Non-Alcoholic,Seltzers" | split: "," -%}
{% for category in categories %}
### {{ category }}

{% assign x = site.data.beer | where: "Category", category -%}
{%- for row in x %}
* **{{ row["Name"] }}**: {% if row["Style"] %}*{{ row["Style"] }}* {% endif %}({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
{% endfor %}
