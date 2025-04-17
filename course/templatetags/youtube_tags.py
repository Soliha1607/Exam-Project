from django import template
import re

register = template.Library()

@register.filter
def extract_youtube_id(url):
    """
    Extract YouTube video ID from a URL
    """
    match = re.search(r'v=([^&]+)', url)
    if match:
        return match.group(1)
    return ''
