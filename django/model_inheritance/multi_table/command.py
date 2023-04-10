from multi_table.models import Location, Restaurant

# it will create a one to one field model relationship for Restaurant table from Location table.
# tables create:
#    - Location
#    - Restaurant


Location.objects.create(name="l", address="adrr")
# id  | name | address
# 1   | l    | "adrr"


Restaurant.objects.create(name="Rest", address="addr2", star=5)

# location table
# id  | name | address
# 1   | l    | "adrr"
# 2   | Rest | "addr2"


# restaurant table
# location_ptr_id | star
#  2              | 5
