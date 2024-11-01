
def get_soc_sec_tax(gross_pay):
    '''Calulate Social Secutiry tax.'''
    tax_rate_sec = .0062
    return round(gross_pay * tax_rate_sec, 2)


def get_medicare_tax(gross_pay):
    '''Calculate Medicare tax.'''
    tax_rate_med = .0145
    return round(gross_pay * tax_rate_med, 2)

def get_federal_tax(gross_pay, withholding_code):
    '''Calculate Federal tax withholding based on the withholding code.'''
    if withholding_code == 0:
        taxrate0 = .23
    elif withholding_code == 1:
        taxrate1 = .21
    elif withholding_code == 2:
        taxrate2 = .195
    elif withholding_code == 3:
        taxrate3 = .185
    elif withholding_code >= 4:
        taxrate4 = .18 - (.005 * (withholding_code - 4))
    else: 
        raise ValueError("Invalid withholding code")

return round(gross_pay * tax_rate_sec, 2)