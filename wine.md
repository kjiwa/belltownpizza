---
layout: page
title: Wine
cover-img: /assets/img/btp-cover-menu.jpg
---

## Sparkling

{% assign x = site.data.wine | where: "Category", "Sparkling" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }} **${{ row["Glass Price"] }}{% if row["Bottle Price"] %}/${{ row["Bottle Price"] }}{% endif %}**
{%- endfor %}

## Rosés

{% assign x = site.data.wine | where: "Category", "Rosés" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }} **${{ row["Glass Price"] }}{% if row["Bottle Price"] %}/${{ row["Bottle Price"] }}{% endif %}**
{%- endfor %}

## Whites

{% assign x = site.data.wine | where: "Category", "Whites" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }} **${{ row["Glass Price"] }}{% if row["Bottle Price"] %}/${{ row["Bottle Price"] }}{% endif %}**
{%- endfor %}

## Reds

{% assign x = site.data.wine | where: "Category", "Reds" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }} **${{ row["Glass Price"] }}{% if row["Bottle Price"] %}/${{ row["Bottle Price"] }}{% endif %}**
{%- endfor %}
