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
    i_ci = math.trunc(data['reportedCases']*10)
    s_ci = math.trunc(data['reportedCases']*50)
    i_ibrtd = math.trunc(i_ci*1.6)
    i_ibrtw = math.trunc(i_ci*5.6)
    i_ibrtm = math.trunc(i_ci*2**10)
    s_ibrtd = math.trunc(i_ci*1.6)
    s_ibrtw = math.trunc(i_ci*5.6)
    s_ibrtm = math.trunc(i_ci*2**10)
    i_ibrt = math.trunc(i_ci*0.6*data["timeToElapse"])
    s_ibrt = math.trunc(s_ci*0.6*data["timeToElapse"])
    i_scbrt = math.trunc(i_ibrt*1.15)
    s_scbrt = math.trunc(s_ibrt*1.15)
    beds = math.trunc(data['totalHospitalBeds']*0.35)
    i_hbrt = math.trunc(beds - i_scbrt)
    s_hbrt = math.trunc(beds - s_scbrt)
    i_icu = math.trunc(i_ibrt*0.05)
    s_icu = math.trunc(s_ibrt*0.05)
    i_rep = math.trunc(s_ibrt*0.02)
    s_rep = math.trunc(s_ibrt*0.02)
    i_dif = math.trunc((data['region']['avgDailyIncomeInUSD']*data['region']
                        ['avgDailyIncomePopulation']*data['timeToElapse']*i_ibrt))
    s_dif = math.trunc((data['region']['avgDailyIncomeInUSD']*data['region']
                        ['avgDailyIncomePopulation']*data['timeToElapse']*s_ibrt))
    data = {
        'data': o_data,
        'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': i_ibrt,
                   'severeCasesByRequestedTime': i_scbrt, 'hospitalBedsByRequestedTime': i_hbrt,
                   'casesForICUByRequestedTime': i_icu,
                   'casesForVentilatorsByRequestedTime': i_rep,
                   'dollarsInFlight': i_dif},
        "severeImpact": {'currentlyInfected': s_ci, 'infectionsByRequestedTime': s_ibrt,
                         'severeCasesByRequestedTime': s_scbrt, 'hospitalBedsByRequestedTime': s_hbrt,
                         'casesForICUByRequestedTime': s_icu,
                         'casesForVentilatorsByRequestedTime': s_rep,
                         'dollarsInFlight': s_dif}}
    # print(data)
    return data
