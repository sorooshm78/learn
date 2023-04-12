from multi_table.models import Location, Restaurant

# it will create a one to one field model relationship for Restaurant table from Location table.
# tables create:
#    - Location
#    - Restaurant


# -------------------------------------------

Location.objects.create(name="loc", address="adrr")
# id  | name | address
# 1   | l    | "adrr"

# -------------------------------------------

Restaurant.objects.create(name="Rest", address="addr2", star=5)

# location table
# id  | name | address
# 1   | loc    | "adrr"
# 2   | Rest | "addr2"


# restaurant table
# location_ptr_id | star
#  2              | 5

# -------------------------------------------
r = Restaurant.objects.filter(name="Rest")[0]

r.name
# Rest

r.address
# 'addr2'

r.star
# 5

# -------------------------------------------

# location table
# id  | name | address
# 1   | loc    | "adrr"
# 2   | Rest | "addr2"

# restaurant table
# location_ptr_id | star
#  2              | 5

Restaurant.objects.create(location_ptr_id=1, star=10)
# <Restaurant: Restaurant object (1)>

# restaurant table
# location_ptr_id | star
#  2              | 5
#  1              | 10


Restaurant.objects.create(location_ptr_id=1, star=66)
# Erorr -> relation is one to one

# -------------------------------------------

# location table
# id  | name | address
# 1   | loc    | "adrr"
# 2   | Rest | "addr2"

# restaurant table
# location_ptr_id | star
#  2              | 5
#  1              | 10

Location.objects.get(id=1).delete()
# on-delete is CASCADE

# location table
# id  | name | address
# 2   | Rest | "addr2"

# restaurant table
# location_ptr_id | star
#  1              | 10

# -------------------------------------------

Location.objects.get(id=2)
# <Location: Rest - addr2>

Restaurant.objects.get(id=2)
# <Restaurant: Rest - addr2 - 5>

# -------------------------------------------
