"""
Body Mass Index (BMI) classification – international vs. Chinese standard.

BMI is defined as:
    BMI = weight (kg) / (height (m))^2

Write a program that:
1. Reads the user's height (in meters) and weight (in kilograms).
2. Computes the BMI value.
3. Classifies the BMI according to BOTH the international and the Chinese
   (domestic) standards:

   International standard:
       - Underweight : BMI < 18.5
       - Normal      : 18.5 <= BMI < 25
       - Overweight  : 25   <= BMI < 30
       - Obese       : BMI >= 30

   Chinese standard:
       - Underweight : BMI < 18.5
       - Normal      : 18.5 <= BMI < 24
       - Overweight  : 24   <= BMI < 28
       - Obese       : BMI >= 28

4. Prints the BMI value rounded to 2 decimal places and outputs both the
   international and Chinese BMI categories for this value.
"""

# body_mass_index_classification.py
height, weight= eval(input("请输入身高（米）和体重（千克），用逗号隔开："))
BMI = weight/pow(height,2)
if BMI < 18.5:
    national, China = '偏瘦', '偏瘦'
elif 18.5 <= BMI < 24:
    national, China = '正常', '正常'
elif 24 <= BMI < 25:
    national, China = '正常', '偏胖'
elif 25 <= BMI < 28:
    national, China = '偏胖', '偏胖'
elif 28 <= BMI < 30:
    national, China = '偏胖', '肥胖'
else:
    national, China = '肥胖', '肥胖'
print("BMI数值为：{:.2f}".format(BMI))
print("BMI指标为：国际'{}'，国内'{}'".format(national,China))
