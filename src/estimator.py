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
    i_scbrt = i_ibrt*1.15
    s_scbrt = s_ibrt*1.15
    beds = data['totalHospitalBeds']*0.35
    i_hbrt = beds - i_scbrt
    s_hbrt = beds - s_scbrt
    i_icu = i_ibrt*0.05
    s_icu = s_ibrt*0.05
    i_rep = s_ibrt*0.02
    s_rep = s_ibrt*0.02
    i_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
             ['avgDailyIncomePopulation']*data['timeToElapse']*i_ibrt)
    s_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
             ['avgDailyIncomePopulation']*data['timeToElapse']*s_ibrt)
    data = {
        'data': o_data,
        'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': math.trunc(i_ibrt),
                   'severeCasesByRequestedTime': math.trunc(i_scbrt), 'hospitalBedsByRequestedTime': math.trunc(i_hbrt),
                   'casesForICUByRequestedTime': math.trunc(i_icu),
                   'casesForVentilatorsByRequestedTime': math.trunc(i_rep),
                   'dollarsInFlight': math.trunc(i_dif)},
        "severeImpact": {'currentlyInfected': s_ci, 'infectionsByRequestedTime': math.trunc(s_ibrt),
                         'severeCasesByRequestedTime': math.trunc(s_scbrt), 'hospitalBedsByRequestedTime': math.trunc(s_hbrt),
                         'casesForICUByRequestedTime': math.trunc(s_icu),
                         'casesForVentilatorsByRequestedTime': math.trunc(s_rep),
                         'dollarsInFlight': math.trunc(s_dif)}}
    # print(data)
    return data


# estimator(covid)
