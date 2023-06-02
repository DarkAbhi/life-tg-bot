import constants


def get_category_id(category):
    match category:
        case constants.ENTERTAINMENT:
            return constants.ENTERTAINMENT_ID
        case constants.SHOPPING:
            return constants.SHOPPING_ID
        case constants.TRANSPORT:
            return constants.TRANSPORT_ID
        case constants.FUEL:
            return constants.FUEL_ID
        case constants.EDUCATION:
            return constants.EDUCATION_ID
        case constants.BILLS_AND_UTILITIES:
            return constants.BILLS_AND_UTILITIES_ID
        case constants.HEALTH_AND_WELLNESS:
            return constants.HEALTH_AND_WELLNESS_ID
        case constants.GROCERIES:
            return constants.GROCERIES_ID
        case constants.TRIPS:
            return constants.TRIPS_ID
        case constants.GADGETS:
            return constants.GADGETS_ID
        case constants.FITNESS:
            return constants.FITNESS_ID
