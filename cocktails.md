---
layout: page
title: Cocktails
cover-img: /assets/img/btp-cover-menu.jpg
---

{% assign categories = "Cocktails,Winter Warmers,Slushies" | split: "," -%}
{% for category in categories %}
## {{ category }}

{% assign x = site.data.cocktails | where: "Category", category -%}
{%- for row in x %}
<h4 class="d-inline-block">{{ row["Name"] }}</h4><div class="float-md-right mt-md-3"><b>${{ row["Price"] }}</b></div>
<p class="mt-0">{{ row["Ingredients"] }}</p>
{%- endfor %}
{% endfor %}
