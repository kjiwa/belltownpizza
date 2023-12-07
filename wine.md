---
layout: page
title: Wine
cover-img: /assets/img/btp-cover-menu.jpg
---

{% assign categories = "Sparkling,Rosés,Whites,Reds" | split: "," -%}
{% for category in categories %}
## {{ category }}

{% assign x = site.data.wine | where: "Category", category -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }} **${{ row["Glass Price"] }}{% if row["Bottle Price"] %}/${{ row["Bottle Price"] }}{% endif %}**
{%- endfor %}
{% endfor %}
