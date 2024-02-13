---
layout: page
title: Spirits
cover-img: /assets/img/btp-cover-menu.jpg
---

{%- assign x = site.data.spirits -%}
{%- assign category = "" -%}
{%- for row in x -%}
{%- assign current_category = row["Category"] -%}
{%- if current_category != category -%}
{% assign category = current_category %}

### {{ category }}
{% endif %}
* {{ row["Name"] }}
{%- endfor -%}
