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

### Domestics

{% assign x = site.data.beer | where: "Category", "Domestics" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
&nbsp;

### Imports

{% assign x = site.data.beer | where: "Category", "Imports" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
&nbsp;

### Locals

{% assign x = site.data.beer | where: "Category", "Locals" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
&nbsp;

### Ciders

{% assign x = site.data.beer | where: "Category", "Ciders" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
&nbsp;

### Non-Alcoholic

{% assign x = site.data.beer | where: "Category", "Non-Alcoholic" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}

### Seltzers

{% assign x = site.data.beer | where: "Category", "Seltzers" -%}
{%- for row in x %}
* **{{ row["Name"] }}**: {{ row["Style"] }} ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{%- endfor %}
&nbsp;
