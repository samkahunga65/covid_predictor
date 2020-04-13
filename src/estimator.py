import math
# covid = {
#     'region': {
#         'name': "Africa",
#         'avgAge': 19.7,
#         'avgDailyIncomeInUSD': 5,
#         'avgDailyIncomePopulation': 0.71
#     },
#     'periodType': "days",
#     'timeToElapse': 2,
#     'reportedCases': 674,
#     'population': 66622705,
#     'totalHospitalBeds': 1380614
# }


def estimator(data):
    o_data = data
    i_ci = data['reportedCases']*10
    s_ci = data['reportedCases']*50
    i_ibrtd = i_ci*1.6
    i_ibrtw = i_ci*5.6
    i_ibrtm = i_ci*2**10
    s_ibrtd = i_ci*1.6
    s_ibrtw = i_ci*5.6
    s_ibrtm = i_ci*2**10
    i_ibrt = i_ci*0.6*data["timeToElapse"]
    s_ibrt = s_ci*0.6*data["timeToElapse"]
    data = {
        'data': o_data,
        'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': math.trunc(i_ibrt)},
        'severeImpact': {'currentlyInfected': s_ci, 'infectionsByRequestedTime': math.trunc(s_ibrt)}}
    print(data)
    return data


# estimator(covid)
