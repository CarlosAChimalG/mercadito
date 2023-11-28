from django_seed import Seed
seeder = Seed.seeder()
    
from api.models import Gender, Rol

seeder.add_entity(Gender, 2, {'nombre': 'Hombre'})
seeder.add_entity(Gender, 2, {'nombre': 'Mujer'})

seeder.add_entity(Rol, 2, {'nombre': 'Administrador'})
seeder.add_entity(Rol, 2, {'nombre': 'Usuario'})

seeder.execute()