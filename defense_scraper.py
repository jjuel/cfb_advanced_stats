import csv
from requests_html import HTMLSession
from datetime import date

TODAY = str(date.today())
DEFENSE_URL = 'https://www.footballoutsiders.com/stats/ncaadef'
ADJ_DEFENSE_FIELDNAMES = [
    'Team',
    'Def_S&P_Plus',
    'Def_S&P_Plus_Rk',
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

DEFENSE_FIELDNAMES = [
    'Team',
    'Success_Rt',
    'Success_Rt_Rk',
    'IsoPPP',
    'IsoPPP_Rk',
    'Havoc',
    'Havoc_Rk',
    'Front_7_Havoc',
    'Front_7_Havoc_Rk',
    'DB_Havoc',
    'DB_Havoc_Rk'
]


def scrape_adj_defense():
    session = HTMLSession()

    resp = session.get(DEFENSE_URL)
    resp.raise_for_status()

    writer = csv.DictWriter(
        open(f'data/adj_defense_{TODAY}.csv', 'w'),
        fieldnames=(ADJ_DEFENSE_FIELDNAMES))
    writer.writeheader()

    defense_table = resp.html.xpath(
        '//table[contains(@class, "stats")][1]/tbody/tr/'
        'td[contains(@align, "right")]/..')

    for team_row in defense_table:
        team = team_row.find('td')[0].text
        def_spp = team_row.find('td')[1].text
        def_spp_rk = team_row.find('td')[2].text
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
            'Def_S&P_Plus': def_spp,
            'Def_S&P_Plus_Rk': def_spp_rk,
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


def scrape_defense():
    session = HTMLSession()

    resp = session.get(DEFENSE_URL)
    resp.raise_for_status()

    writer = csv.DictWriter(
        open(f'data/unadj_defense_{TODAY}.csv', 'w'),
        fieldnames=(DEFENSE_FIELDNAMES))
    writer.writeheader()

    defense_table = resp.html.xpath(
        '//table[contains(@class, "stats")][2]/tbody/tr/'
        'td[contains(@align, "right")]/..')

    for team_row in defense_table:
        team = team_row.find('td')[0].text
        succ_rt = team_row.find('td')[3].text
        succ_rt_rk = team_row.find('td')[4].text
        isoppp = team_row.find('td')[5].text
        isoppp_rk = team_row.find('td')[6].text
        havoc = team_row.find('td')[7].text
        havoc_rk = team_row.find('td')[8].text
        front_7_havoc = team_row.find('td')[9].text
        front_7_havoc_rk = team_row.find('td')[10].text
        db_havoc = team_row.find('td')[11].text
        db_havoc_rk = team_row.find('td')[12].text

        row = {
            'Team': team,
            'Success_Rt': succ_rt,
            'Success_Rt_Rk': succ_rt_rk,
            'IsoPPP': isoppp,
            'IsoPPP_Rk': isoppp_rk,
            'Havoc': havoc,
            'Havoc_Rk': havoc_rk,
            'Front_7_Havoc': front_7_havoc,
            'Front_7_Havoc_Rk': front_7_havoc_rk,
            'DB_Havoc': db_havoc,
            'DB_Havoc_Rk': db_havoc_rk
        }

        writer.writerow(row)


if __name__ == '__main__':
    scrape_adj_defense()
    scrape_defense()
