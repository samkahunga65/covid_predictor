
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
    return data
