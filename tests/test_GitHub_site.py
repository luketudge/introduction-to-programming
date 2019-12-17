# -*- coding: utf-8 -*-

# %% Page names

TOPIC_PAGE = 'Topic listing'

TOPICS = ['Creating a computer program with Python',
          'Variables and data types',
          'Sequences and mappings',
          'Conditions',
          'Iteration',
          'Functions',
          'Modules',
          'The standard library',
          'Files']

OTHER_PAGES = ['Software',
               'Readings',
               'Example programs',
               'Glossary',
               'Contributing']


# %% Files

EXAMPLE_FILES = ['age_next_year.py',
                 'greeting.py',
                 'ids.py',
                 'make_monthly_directories.py',
                 'alternative_ending.py',
                 'fun_facts.py',
                 'guess_the_animal.py',
                 'initials.py',
                 'my_program.py',
                 'slim_shady.py',
                 'circle.py',
                 'greeting_personal.py',
                 'hoff.py',
                 'name_trivia.py']

DATA_FILES = ['austen-sense.txt',
              'melville-moby_dick.txt',
              'penguins_DE.csv',
              'top_10_bands.txt',
              'top_5_bands_UTF8.txt',
              'guardian_taramasalata.json',
              'penguins.csv',
              'README.md',
              'top_5_bands_LATIN1.txt']

DATA_FILES = ['data/' + f for f in DATA_FILES]


# %% Helper function

def click_link(b, link_text):

    b.find_element_by_link_text(link_text).click()


# %% Test functions

def test_main_page(browser):

    # Are we starting on the main page?
    assert 'introduction-to-programming' in browser.title


def test_topic_pages(browser):

    # Navigate to the topics page.
    click_link(browser, TOPIC_PAGE)

    # Visit each of the topic pages.
    for topic in TOPICS:

        click_link(browser, topic)

        # Did we get it?
        assert topic in browser.page_source

        # Does it have a table of contents?
        assert 'Contents' in browser.page_source

        browser.back()


def test_other_pages(browser):

    # Visit each of the other pages.
    for page in OTHER_PAGES:

        click_link(browser, page)

        # Did we get it?
        assert page in browser.page_source

        browser.back()


def test_zip_download(file):

    contents = file.namelist()

    assert set(contents) == set(EXAMPLE_FILES + DATA_FILES)
