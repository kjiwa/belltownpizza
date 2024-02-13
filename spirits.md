---
layout: page
title: Spirits
cover-img: /assets/img/btp-cover-menu.jpg
---

<ul class="nav justify-content-center sticky-top pt-5 bg-white small">
{% assign category = "" %}
{% for row in site.data.spirits %}
{% assign current_category = row["Category"] %}
{% if current_category != category %}
{% assign category = current_category %}
  <li class="nav-item"><a class="nav-link" href="#{{ category | replace: " ", "-" | downcase }}">{{ category }}</a></li>
{% endif %}
{% endfor %}
</ul>

{%- assign category = "" -%}
{%- for row in site.data.spirits -%}
{%- assign current_category = row["Category"] -%}
{%- if current_category != category -%}
{% assign category = current_category %}

### {{ category }}
{% endif %}
* <div class="w-100 d-flex justify-content-between"><strong>{{ row["Name"] }}</strong> {% if row["Price"] %}<span class="text-right">${{ row["Price"] }}</span>{% endif %}</div>
{%- endfor -%}
