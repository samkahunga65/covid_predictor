covid = {
    'region': {
        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}


def estimator(data):
    o_data = data
    i_ci = data['reportedCases']*10
    s_ci = data['reportedCases']*50
    i_ibrt = i_ci*2**3
    s_ibrt = s_ci*2**3

    data = {
        'data': o_data,
        'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': i_ibrt, },
        'severeImpact': {'currentlyInfected': s_ci, 'infectionsByRequestedTime': s_ibrt, }}
    print(data)
    return data


estimator(covid)
