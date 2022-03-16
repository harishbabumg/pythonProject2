list_ = ["ಅಂಕ ಗುರುತು, ತೊಡೆ, ಹೆಸರು, ಯುದ್ಧ, ನಾಟಕದಲ್ಲಿ ಒಂದು ವಿಭಾಗ ನಾಮವಾಚಕ"]
dd={}
# list_ = []
for element in list_:
    st = element.split(" ")
    a, *rest, b = st
    dd[a] = rest

print(dd)