public class Calculator {
public static Integer add(Integer a, Integer b) {
if (a == 10) {
return 10;
}
return a+b;
}
# use only with Jython

#import Calculator
print(Calculator.add(4, 8))
print(Calculator.add(10, 8))