# Variables for collection names
v_nameCollection = 'VakaSaikumar'
v_phoneCollection = '8008318245'  
# Create collections
createCollection(v_nameCollection)  
createCollection(v_phoneCollection)

# Get employee count (before indexing)
getEmpCount(v_nameCollection)

# Index data excluding specified columns
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

# Delete employee by ID
delEmpById(v_nameCollection, 'E02003')

# Get employee count (after deletion)
getEmpCount(v_nameCollection)

# Search by column
searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

# Get department facets
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
