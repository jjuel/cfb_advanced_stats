import csv
from requests_html import HTMLSession
from datetime import date

TODAY = str(date.today())
OVERALL_URL = 'https://www.footballoutsiders.com/stats/ncaa'
OVERALL_FIELDNAMES = [
    'Team',
    'Conference',
    'Record',
    '2nd_Order_Wins_Diff',
    'S&P_Plus_Pctile',
    'S&P_Plus_Rtg',
    'S&P_Plus_Rk',
    'Off_S&P_Plus',
    'Off_S&P_Plus_Rk',
    'Def_S&P_Plus',
    'Def_S&P_Plus_Rk',
    'ST_S&P_Plus',
    'ST_S&P_Plus_Rk',
    'SOS',
    'SOS_Rk'
]


def scrape_overall():
    session = HTMLSession()

    resp = session.get(OVERALL_URL)
    resp.raise_for_status()

    writer = csv.DictWriter(
        open(f'data/overall_{TODAY}.csv', 'w'),
        fieldnames=(OVERALL_FIELDNAMES))
    writer.writeheader()

    overall_table = resp.html.xpath(
        '//table[contains(@class, "stats")][1]/tbody/tr/'
        'td/..')

    for team_row in overall_table:
        team = team_row.find('td')[0].text
        conf = team_row.find('td')[1].text
        record = team_row.find('td')[2].text
        scnd_ord_wins = team_row.find('td')[3].text
        spp_pctile = team_row.find('td')[4].text
        spp_rating = team_row.find('td')[5].text
        spp_rk = team_row.find('td')[6].text
        off_spp = team_row.find('td')[7].text
        off_spp_rk = team_row.find('td')[8].text
        def_spp = team_row.find('td')[9].text
        def_spp_rk = team_row.find('td')[10].text
        st_spp = team_row.find('td')[11].text
        st_spp_rk = team_row.find('td')[12].text
        sos = team_row.find('td')[13].text
        sos_rk = team_row.find('td')[14].text

        row = {
            'Team': team,
            'Conference': conf,
            'Record': record,
            '2nd_Order_Wins_Diff': scnd_ord_wins,
            'S&P_Plus_Pctile': spp_pctile,
            'S&P_Plus_Rtg': spp_rating,
            'S&P_Plus_Rk': spp_rk,
            'Off_S&P_Plus': off_spp,
            'Off_S&P_Plus_Rk': off_spp_rk,
            'Def_S&P_Plus': def_spp,
            'Def_S&P_Plus_Rk': def_spp_rk,
            'ST_S&P_Plus': st_spp,
            'ST_S&P_Plus_Rk': st_spp_rk,
            'SOS': sos,
            'SOS_Rk': sos_rk
        }

        writer.writerow(row)


if __name__ == '__main__':
    scrape_overall()
