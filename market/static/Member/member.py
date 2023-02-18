from market.models import Member


def validateMember(mem):

    m = Member.query.filter_by(id = mem).first()

    if m:
        return 'Pass'
    else:
        return 'Fail'