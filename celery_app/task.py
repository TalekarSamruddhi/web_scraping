import os
import csv
from typing import List
from celery import shared_task
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@shared_task
def sleepy(duration):
    sleep(duration)
    print('Duration=====', duration)


@shared_task
def scrape_data(url):
    print(f"Start scraping for {url}...")
    fields = ['version', 'status', 'release', 'end-of-support']
    with open("./scraped.csv", mode='a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

    driver = Chrome(
        executable_path=os.path.join(os.getcwd(), 'celery_app/chromedriver')
    )
    driver.get(url=url)
    lists = driver.find_elements(
        By.CSS_SELECTOR, ".active-release-list-widget .list-row-container")
    for list in lists:
        for item in list.find_elements(By.TAG_NAME, "li"):
            version = item.find_element(By.CLASS_NAME, "release-version")
            status = item.find_element(By.CLASS_NAME, "release-status")
            release = item.find_element(By.CLASS_NAME, "release-start")
            endof_support = item.find_element(By.CLASS_NAME, "release-end")

            row = [[version.text, status.text,
                   release.text, endof_support.text]]
            with open("./scraped.csv", mode='a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(row)
    csvfile.close()

    return None
