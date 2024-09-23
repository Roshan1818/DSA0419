import numpy as np
fuel_efficiency = np.array([25, 30, 22, 35, 28, 40])
average_fuel_efficiency = np.mean(fuel_efficiency)
old_model_efficiency = fuel_efficiency[0]
new_model_efficiency = fuel_efficiency[5]
percentage_improvement = ((new_model_efficiency - old_model_efficiency) / old_model_efficiency) * 100
print("Average fuel efficiency:", average_fuel_efficiency)
print("Percentage improvement between model 1 and model 6:", percentage_improvement)
