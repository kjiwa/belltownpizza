---
layout: page
title: Cocktails
cover-img: /assets/img/btp-cover-menu.jpg
---

<ul class="nav justify-content-center sticky-top pt-5 bg-white small">
{% assign category = "" %}
{% for row in site.data.cocktails %}
{% assign current_category = row["Category"] %}
{% if current_category != category %}
{% assign category = current_category %}
  <li class="nav-item"><a class="nav-link" href="#{{ category | replace: " ", "-" | downcase }}">{{ category }}</a></li>
{% endif %}
{% endfor %}
</ul>

{%- assign category = "" -%}
{%- for row in site.data.cocktails -%}
{%- assign current_category = row["Category"] -%}
{%- if current_category != category -%}
{% assign category = current_category %}

## {{ category }}
{% endif %}
<h4 class="d-inline-block">{{ row["Name"] }}</h4><div class="float-md-right mt-md-3"><b>${{ row["Price"] }}</b></div>
<p class="m-0">{{ row["Ingredients"] }}</p>
{%- endfor -%}
