import csv
from requests_html import HTMLSession
from datetime import date

TODAY = str(date.today())
OFFENSE_URL = 'https://www.footballoutsiders.com/stats/ncaaoff'
ADJ_OFFENSE_FIELDNAMES = [
    'Team',
    'Off_S&P_Plus',
    'Off_S&P_Plus_Rk',
    'Success_Rt_Plus',
    'Success_Rt_Plus_Rk',
    'IsoPPP_Plus',
    'IsoPPP_Plus_Rk',
    'Rushing_S&P_Plus',
    'Rushing_S&P_Plus_Rk',
    'Passing_S&P_Plus',
    'Passing_S&P_Plus_Rk',
    'SD_S&P_Plus',
    'SD_S&P_Plus_Rk',
    'PD_S&P_Plus',
    'PD_S&P_Plus_Rk'
]

OFFENSE_FIELDNAMES = [
    'Team',
    'Success_Rt',
    'Success_Rt_Rk',
    'IsoPPP',
    'IsoPPP_Rk',
    'Adj_Run_Rate',
    'Adj_Run_Rate_Rk',
    'Adj_Pace',
    'Adj_Pace_Rk'
]


def scrape_adj_offense():
    session = HTMLSession()

    resp = session.get(OFFENSE_URL)
    resp.raise_for_status()

    writer = csv.DictWriter(
        open(f'data/adj_offense_{TODAY}.csv', 'w'),
        fieldnames=(ADJ_OFFENSE_FIELDNAMES))
    writer.writeheader()

    offense_table = resp.html.xpath(
        '//table[contains(@class, "stats")][1]/tbody/tr/'
        'td[contains(@align, "right")]/..')

    for team_row in offense_table:
        team = team_row.find('td')[0].text
        off_spp = team_row.find('td')[1].text
        off_spp_rk = team_row.find('td')[2].text
        succ_rt = team_row.find('td')[3].text
        succ_rt_rk = team_row.find('td')[4].text
        isoppp_p = team_row.find('td')[5].text
        isoppp_p_rk = team_row.find('td')[6].text
        rushing_spp = team_row.find('td')[7].text
        rushing_spp_rk = team_row.find('td')[8].text
        passing_spp = team_row.find('td')[9].text
        passing_spp_rk = team_row.find('td')[10].text
        sd_spp = team_row.find('td')[11].text
        sd_spp_rk = team_row.find('td')[12].text
        pd_spp = team_row.find('td')[13].text
        pd_spp_rk = team_row.find('td')[14].text

        row = {
            'Team': team,
            'Off_S&P_Plus': off_spp,
            'Off_S&P_Plus_Rk': off_spp_rk,
            'Success_Rt_Plus': succ_rt,
            'Success_Rt_Plus_Rk': succ_rt_rk,
            'IsoPPP_Plus': isoppp_p,
            'IsoPPP_Plus_Rk': isoppp_p_rk,
            'Rushing_S&P_Plus': rushing_spp,
            'Rushing_S&P_Plus_Rk': rushing_spp_rk,
            'Passing_S&P_Plus': passing_spp,
            'Passing_S&P_Plus_Rk': passing_spp_rk,
            'SD_S&P_Plus': sd_spp,
            'SD_S&P_Plus_Rk': sd_spp_rk,
            'PD_S&P_Plus': pd_spp,
            'PD_S&P_Plus_Rk': pd_spp_rk
        }

        writer.writerow(row)


def scrape_offense():
    session = HTMLSession()

    resp = session.get(OFFENSE_URL)
    resp.raise_for_status()

    writer = csv.DictWriter(
        open(f'data/unadj_offense_{TODAY}.csv', 'w'),
        fieldnames=(OFFENSE_FIELDNAMES))
    writer.writeheader()

    offense_table = resp.html.xpath(
        '//table[contains(@class, "stats")][2]/tbody/tr/'
        'td[contains(@align, "right")]/..')

    for team_row in offense_table:
        team = team_row.find('td')[0].text
        succ_rt = team_row.find('td')[3].text
        succ_rt_rk = team_row.find('td')[4].text
        isoppp = team_row.find('td')[5].text
        isoppp_rk = team_row.find('td')[6].text
        adj_run_rate = team_row.find('td')[7].text
        adj_run_rate_rk = team_row.find('td')[8].text
        adj_pace = team_row.find('td')[9].text
        adj_pace_rk = team_row.find('td')[10].text

        row = {
            'Team': team,
            'Success_Rt': succ_rt,
            'Success_Rt_Rk': succ_rt_rk,
            'IsoPPP': isoppp,
            'IsoPPP_Rk': isoppp_rk,
            'Adj_Run_Rate': adj_run_rate,
            'Adj_Run_Rate_Rk': adj_run_rate_rk,
            'Adj_Pace': adj_pace,
            'Adj_Pace_Rk': adj_pace_rk
        }

        writer.writerow(row)


if __name__ == '__main__':
    scrape_adj_offense()
    scrape_offense()
