---
layout: page
title: Beer
cover-img: /assets/img/btp-cover-menu.jpg
---

## Drafts

{% for row in site.data.beer -%}
{% if row["Category"] == "Drafts" -%}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;
* Rotating Cider
* Rotating IPA
* Rotating Pale Ale
* Rotating Pilsner
* Rotating Seasonal Draft

## Bottled/Canned Beer, Cider, and Seltzers

### Domestics

{% for row in site.data.beer -%}
{% if row["Category"] == "Domestics" -%}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;

### Imports

{% for row in site.data.beer -%}
{% if row["Category"] == "Imports" -%}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;

### Locals

{% for row in site.data.beer -%}
{% if row["Category"] == "Locals" -%}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;

### Ciders

{% for row in site.data.beer -%}
{% if row["Category"] == "Ciders" -%}
* **{{ row["Name"] }}**: ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;

### Non-Alcoholic

{% for row in site.data.beer -%}
{% if row["Category"] == "Non-Alcoholic" -%}
* **{{ row["Name"] }}**: *{{ row["Style"] }}* ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;

### Seltzers

{% for row in site.data.beer -%}
{% if row["Category"] == "Seltzers" -%}
* **{{ row["Name"] }}**: {{ row["Style"] }} ({{ row["ABV"] }}% ABV) {{ row["Origin"] }}
{% endif -%}
{% endfor -%}
&nbsp;
