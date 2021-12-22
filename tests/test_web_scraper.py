from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'

# Test scraper's citations needed count function returns count.
def test_scraper_count_randal_monroe():
    url = "https://en.wikipedia.org/wiki/Randall_Munroe"
    assert get_citations_needed_count(url) == 2

# Test scraper's citations report returns a new line deliminated string of passages that need citations.
def test_scraper_passages_randal_monroe():
    url = "https://en.wikipedia.org/wiki/Randall_Munroe"
    
    assert get_citations_needed_report(url).split('\n')[0] == 'Munroe is the creator of the now defunct websites "The Funniest",[19] "The Cutest",[20] and "The Fairest",[21] each of which presents users with two options and asks them to choose one over the other.[citation needed]'

    assert get_citations_needed_report(url).split('\n')[1] == 'In response to concerns about the radioactivity released by the Fukushima Daiichi nuclear disaster in 2011, and to remedy what he described as "confusing" reporting on radiation levels in the media, Munroe created a radiation chart of comparative radiation exposure levels.[30] The chart was rapidly adopted by print and online journalists in several countries,[citation needed] including being linked to by online writers for The Guardian,[31] and The New York Times.[32] As a result of requests for permission to reprint the chart and to translate it into Japanese, Munroe placed it in the public domain, but requested that his non-expert status should be clearly stated in any reprinting.[33]'