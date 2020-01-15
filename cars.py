showroom = {'Toyota Tacoma', 'Land Rover Defender', 'Toyota Landcruiser','Ford Bronco'}

print(len(showroom))

showroom.add('Toyota Tacoma')

print(showroom)

showroom.update(['Shelby Cobra', 'Aston Martin DB11'])

showroom.discard('Toyota Tacoma')

print(showroom)


junkyard = {'Pontiac Firebird', 'Ford Mustang', 'Chevrolet Camaro', 'Audi R8', 'Ford Bronco', 'Land Rover Defender', 'Toyota Landcruiser'}

print(showroom.intersection(junkyard))

new_showroom = showroom.union(junkyard)

print(new_showroom)