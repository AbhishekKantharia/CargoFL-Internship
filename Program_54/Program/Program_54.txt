# Import the pgeocode module using the import keyword
import pgeocode
# Pass some random country name to the Nominatim() function to query country given
# Store it in a variable
# Here 'fr' means France - to check for other country code see the Readme list of 
# pgeocode module
cntry_data = pgeocode.Nominatim('fr')
# Pass some random postal code to the query_postal_code() function to
# get the information (like country code, state, name) about the region given.
# Store it in another variable
rslt_info = cntry_data.query_postal_code("75013")
# Print the above result.
print(rslt_info)