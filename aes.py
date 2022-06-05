__all__ = ['aes']

import base64

from js2py.pyjs import *

var = Scope( JS_BUILTINS )
set_global_object(var)

var.registers(['base64Decode', 'Aes', 'base64Encode'])
@Js
def PyJsHoisted_base64Encode_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['ww', 'w', 'i'])
    var.put('ww', var.get('Array').create(var.get('w').get('length')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('w').get('length')):
        try:
            var.get('ww').put(var.get('i'), var.get('w').callprop('charCodeAt', var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    ee = list()
    for ei in range(int(var.get('w').get('length').value)):
        ww = var.get('ww')[ei]
        ee.append(    int(ww.value)     )
    return base64.b64encode(bytes(ee)).decode('ascii')
PyJsHoisted_base64Encode_.func_name = 'base64Encode'
var.put('base64Encode', PyJsHoisted_base64Encode_)
@Js
def PyJsHoisted_base64Decode_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['w'])
    prt = base64.b64decode(  str(var.get('w').value).encode('ascii'))
    wwty = str()
    for ert in range(len(prt)):
        wwty += chr(prt[ert])
    return wwty
PyJsHoisted_base64Decode_.func_name = 'base64Decode'
var.put('base64Decode', PyJsHoisted_base64Decode_)
var.put('Aes', Js({}))
@Js
def PyJs_anonymous_0_(input, w, this, arguments, var=var):
    var = Scope({'input':input, 'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['round', 'input', 'w', 'output', 'Nr', 'Nb', 'i', 'state'])
    var.put('Nb', Js(4.0))
    var.put('Nr', ((var.get('w').get('length')/var.get('Nb'))-Js(1.0)))
    var.put('state', Js([Js([]), Js([]), Js([]), Js([])]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(Js(4.0)*var.get('Nb'))):
        try:
            var.get('state').get((var.get('i')%Js(4.0))).put(var.get('Math').callprop('floor', (var.get('i')/Js(4.0))), var.get('input').get(var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('state', var.get('Aes').callprop('addRoundKey', var.get('state'), var.get('w'), Js(0.0), var.get('Nb')))
    #for JS loop
    var.put('round', Js(1.0))
    while (var.get('round')<var.get('Nr')):
        try:
            var.put('state', var.get('Aes').callprop('subBytes', var.get('state'), var.get('Nb')))
            var.put('state', var.get('Aes').callprop('shiftRows', var.get('state'), var.get('Nb')))
            var.put('state', var.get('Aes').callprop('mixColumns', var.get('state'), var.get('Nb')))
            var.put('state', var.get('Aes').callprop('addRoundKey', var.get('state'), var.get('w'), var.get('round'), var.get('Nb')))
        finally:
                (var.put('round',Js(var.get('round').to_number())+Js(1))-Js(1))
    var.put('state', var.get('Aes').callprop('subBytes', var.get('state'), var.get('Nb')))
    var.put('state', var.get('Aes').callprop('shiftRows', var.get('state'), var.get('Nb')))
    var.put('state', var.get('Aes').callprop('addRoundKey', var.get('state'), var.get('w'), var.get('Nr'), var.get('Nb')))
    var.put('output', var.get('Array').create((Js(4.0)*var.get('Nb'))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(Js(4.0)*var.get('Nb'))):
        try:
            var.get('output').put(var.get('i'), var.get('state').get((var.get('i')%Js(4.0))).get(var.get('Math').callprop('floor', (var.get('i')/Js(4.0)))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('output')
PyJs_anonymous_0_._set_name('anonymous')
var.get('Aes').put('cipher', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_1_(key, this, arguments, var=var):
    var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 't', 'r', 'key', 'Nr', 'Nk', 'Nb', 'i', 'temp'])
    var.put('Nb', Js(4.0))
    var.put('Nk', (var.get('key').get('length')/Js(4.0)))
    var.put('Nr', (var.get('Nk')+Js(6.0)))
    var.put('w', var.get('Array').create((var.get('Nb')*(var.get('Nr')+Js(1.0)))))
    var.put('temp', var.get('Array').create(Js(4.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('Nk')):
        try:
            var.put('r', Js([var.get('key').get((Js(4.0)*var.get('i'))), var.get('key').get(((Js(4.0)*var.get('i'))+Js(1.0))), var.get('key').get(((Js(4.0)*var.get('i'))+Js(2.0))), var.get('key').get(((Js(4.0)*var.get('i'))+Js(3.0)))]))
            var.get('w').put(var.get('i'), var.get('r'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', var.get('Nk'))
    while (var.get('i')<(var.get('Nb')*(var.get('Nr')+Js(1.0)))):
        try:
            var.get('w').put(var.get('i'), var.get('Array').create(Js(4.0)))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<Js(4.0)):
                try:
                    var.get('temp').put(var.get('t'), var.get('w').get((var.get('i')-Js(1.0))).get(var.get('t')))
                finally:
                        (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
            if ((var.get('i')%var.get('Nk'))==Js(0.0)):
                var.put('temp', var.get('Aes').callprop('subWord', var.get('Aes').callprop('rotWord', var.get('temp'))))
                #for JS loop
                var.put('t', Js(0.0))
                while (var.get('t')<Js(4.0)):
                    try:
                        var.get('temp').put(var.get('t'), var.get('Aes').get('rCon').get((var.get('i')/var.get('Nk'))).get(var.get('t')), '^')
                    finally:
                            (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
            else:
                if ((var.get('Nk')>Js(6.0)) and ((var.get('i')%var.get('Nk'))==Js(4.0))):
                    var.put('temp', var.get('Aes').callprop('subWord', var.get('temp')))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<Js(4.0)):
                try:
                    var.get('w').get(var.get('i')).put(var.get('t'), (var.get('w').get((var.get('i')-var.get('Nk'))).get(var.get('t'))^var.get('temp').get(var.get('t'))))
                finally:
                        (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('w')
PyJs_anonymous_1_._set_name('anonymous')
var.get('Aes').put('keyExpansion', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(s, Nb, this, arguments, var=var):
    var = Scope({'s':s, 'Nb':Nb, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 's', 'c', 'Nb'])
    #for JS loop
    var.put('r', Js(0.0))
    while (var.get('r')<Js(4.0)):
        try:
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<var.get('Nb')):
                try:
                    var.get('s').get(var.get('r')).put(var.get('c'), var.get('Aes').get('sBox').get(var.get('s').get(var.get('r')).get(var.get('c'))))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
        finally:
                (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
    return var.get('s')
PyJs_anonymous_2_._set_name('anonymous')
var.get('Aes').put('subBytes', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(s, Nb, this, arguments, var=var):
    var = Scope({'s':s, 'Nb':Nb, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'c', 'r', 'Nb', 's'])
    var.put('t', var.get('Array').create(Js(4.0)))
    #for JS loop
    var.put('r', Js(1.0))
    while (var.get('r')<Js(4.0)):
        try:
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('t').put(var.get('c'), var.get('s').get(var.get('r')).get(((var.get('c')+var.get('r'))%var.get('Nb'))))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('s').get(var.get('r')).put(var.get('c'), var.get('t').get(var.get('c')))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
        finally:
                (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
    return var.get('s')
PyJs_anonymous_3_._set_name('anonymous')
var.get('Aes').put('shiftRows', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_4_(s, Nb, this, arguments, var=var):
    var = Scope({'s':s, 'Nb':Nb, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'c', 'a', 'Nb', 'i', 's'])
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<Js(4.0)):
        try:
            var.put('a', var.get('Array').create(Js(4.0)))
            var.put('b', var.get('Array').create(Js(4.0)))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(4.0)):
                try:
                    var.get('a').put(var.get('i'), var.get('s').get(var.get('i')).get(var.get('c')))
                    var.get('b').put(var.get('i'), (((var.get('s').get(var.get('i')).get(var.get('c'))<<Js(1.0))^Js(283)) if (var.get('s').get(var.get('i')).get(var.get('c'))&Js(128)) else (var.get('s').get(var.get('i')).get(var.get('c'))<<Js(1.0))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('s').get('0').put(var.get('c'), ((((var.get('b').get('0')^var.get('a').get('1'))^var.get('b').get('1'))^var.get('a').get('2'))^var.get('a').get('3')))
            var.get('s').get('1').put(var.get('c'), ((((var.get('a').get('0')^var.get('b').get('1'))^var.get('a').get('2'))^var.get('b').get('2'))^var.get('a').get('3')))
            var.get('s').get('2').put(var.get('c'), ((((var.get('a').get('0')^var.get('a').get('1'))^var.get('b').get('2'))^var.get('a').get('3'))^var.get('b').get('3')))
            var.get('s').get('3').put(var.get('c'), ((((var.get('a').get('0')^var.get('b').get('0'))^var.get('a').get('1'))^var.get('a').get('2'))^var.get('b').get('3')))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    return var.get('s')
PyJs_anonymous_4_._set_name('anonymous')
var.get('Aes').put('mixColumns', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_5_(state, w, rnd, Nb, this, arguments, var=var):
    var = Scope({'state':state, 'w':w, 'rnd':rnd, 'Nb':Nb, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'rnd', 'c', 'r', 'Nb', 'state'])
    #for JS loop
    var.put('r', Js(0.0))
    while (var.get('r')<Js(4.0)):
        try:
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<var.get('Nb')):
                try:
                    var.get('state').get(var.get('r')).put(var.get('c'), var.get('w').get(((var.get('rnd')*Js(4.0))+var.get('c'))).get(var.get('r')), '^')
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
        finally:
                (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
    return var.get('state')
PyJs_anonymous_5_._set_name('anonymous')
var.get('Aes').put('addRoundKey', PyJs_anonymous_5_)
@Js
def PyJs_anonymous_6_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'i'])
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        try:
            var.get('w').put(var.get('i'), var.get('Aes').get('sBox').get(var.get('w').get(var.get('i'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('w')
PyJs_anonymous_6_._set_name('anonymous')
var.get('Aes').put('subWord', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'i', 'tmp'])
    var.put('tmp', var.get('w').get('0'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(3.0)):
        try:
            var.get('w').put(var.get('i'), var.get('w').get((var.get('i')+Js(1.0))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('w').put('3', var.get('tmp'))
    return var.get('w')
PyJs_anonymous_7_._set_name('anonymous')
var.get('Aes').put('rotWord', PyJs_anonymous_7_)
def PyJs_LONG_8_(var=var):
    return var.get('Aes').put('sBox', Js([Js(99), Js(124), Js(119), Js(123), Js(242), Js(107), Js(111), Js(197), Js(48), Js(1), Js(103), Js(43), Js(254), Js(215), Js(171), Js(118), Js(202), Js(130), Js(201), Js(125), Js(250), Js(89), Js(71), Js(240), Js(173), Js(212), Js(162), Js(175), Js(156), Js(164), Js(114), Js(192), Js(183), Js(253), Js(147), Js(38), Js(54), Js(63), Js(247), Js(204), Js(52), Js(165), Js(229), Js(241), Js(113), Js(216), Js(49), Js(21), Js(4), Js(199), Js(35), Js(195), Js(24), Js(150), Js(5), Js(154), Js(7), Js(18), Js(128), Js(226), Js(235), Js(39), Js(178), Js(117), Js(9), Js(131), Js(44), Js(26), Js(27), Js(110), Js(90), Js(160), Js(82), Js(59), Js(214), Js(179), Js(41), Js(227), Js(47), Js(132), Js(83), Js(209), Js(0), Js(237), Js(32), Js(252), Js(177), Js(91), Js(106), Js(203), Js(190), Js(57), Js(74), Js(76), Js(88), Js(207), Js(208), Js(239), Js(170), Js(251), Js(67), Js(77), Js(51), Js(133), Js(69), Js(249), Js(2), Js(127), Js(80), Js(60), Js(159), Js(168), Js(81), Js(163), Js(64), Js(143), Js(146), Js(157), Js(56), Js(245), Js(188), Js(182), Js(218), Js(33), Js(16), Js(255), Js(243), Js(210), Js(205), Js(12), Js(19), Js(236), Js(95), Js(151), Js(68), Js(23), Js(196), Js(167), Js(126), Js(61), Js(100), Js(93), Js(25), Js(115), Js(96), Js(129), Js(79), Js(220), Js(34), Js(42), Js(144), Js(136), Js(70), Js(238), Js(184), Js(20), Js(222), Js(94), Js(11), Js(219), Js(224), Js(50), Js(58), Js(10), Js(73), Js(6), Js(36), Js(92), Js(194), Js(211), Js(172), Js(98), Js(145), Js(149), Js(228), Js(121), Js(231), Js(200), Js(55), Js(109), Js(141), Js(213), Js(78), Js(169), Js(108), Js(86), Js(244), Js(234), Js(101), Js(122), Js(174), Js(8), Js(186), Js(120), Js(37), Js(46), Js(28), Js(166), Js(180), Js(198), Js(232), Js(221), Js(116), Js(31), Js(75), Js(189), Js(139), Js(138), Js(112), Js(62), Js(181), Js(102), Js(72), Js(3), Js(246), Js(14), Js(97), Js(53), Js(87), Js(185), Js(134), Js(193), Js(29), Js(158), Js(225), Js(248), Js(152), Js(17), Js(105), Js(217), Js(142), Js(148), Js(155), Js(30), Js(135), Js(233), Js(206), Js(85), Js(40), Js(223), Js(140), Js(161), Js(137), Js(13), Js(191), Js(230), Js(66), Js(104), Js(65), Js(153), Js(45), Js(15), Js(176), Js(84), Js(187), Js(22)]))
PyJs_LONG_8_()
def PyJs_LONG_9_(var=var):
    return var.get('Aes').put('rCon', Js([Js([Js(0), Js(0), Js(0), Js(0)]), Js([Js(1), Js(0), Js(0), Js(0)]), Js([Js(2), Js(0), Js(0), Js(0)]), Js([Js(4), Js(0), Js(0), Js(0)]), Js([Js(8), Js(0), Js(0), Js(0)]), Js([Js(16), Js(0), Js(0), Js(0)]), Js([Js(32), Js(0), Js(0), Js(0)]), Js([Js(64), Js(0), Js(0), Js(0)]), Js([Js(128), Js(0), Js(0), Js(0)]), Js([Js(27), Js(0), Js(0), Js(0)]), Js([Js(54), Js(0), Js(0), Js(0)])]))
PyJs_LONG_9_()
var.get('Aes').put('Ctr', Js({}))
pass
@Js
def PyJs_anonymous_10_(plaintext, password, nBits, this, arguments, var=var):
    var = Scope({'plaintext':plaintext, 'password':password, 'nBits':nBits, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'keySchedule', 'counterBlock', 'nonceMs', 'nonceSec', 'nonce', 'blockCount', 'ctrTxt', 'b', 'blockLength', 'password', 'nonceRnd', 'key', 'nBits', 'pwBytes', 'i', 'plaintext', 'nBytes', 'blockSize', 'cipherCntr', 'ciphertext', 'cipherChar'])
    var.put('blockSize', Js(16.0))
    if (((var.get('nBits')==Js(128.0)) or (var.get('nBits')==Js(192.0))) or (var.get('nBits')==Js(256.0))).neg():
        PyJsTempException = JsToPyException(var.get('Error').create(Js('Key size is not 128 / 192 / 256')))
        raise PyJsTempException
    var.put('nBytes', (var.get('nBits')/Js(8.0)))
    var.put('pwBytes', var.get('Array').create(var.get('nBytes')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('nBytes')):
        try:
            var.get('pwBytes').put(var.get('i'), (var.get('password').callprop('charCodeAt', var.get('i')) if (var.get('i')<var.get('password').get('length')) else Js(0.0)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('key', var.get('Aes').callprop('cipher', var.get('pwBytes'), var.get('Aes').callprop('keyExpansion', var.get('pwBytes'))))
    var.put('key', var.get('key').callprop('concat', var.get('key').callprop('slice', Js(0.0), (var.get('nBytes')-Js(16.0)))))
    var.put('counterBlock', var.get('Array').create(var.get('blockSize')))
    var.put('nonce', var.get('Date').create().callprop('getTime'))
    var.put('nonceMs', (var.get('nonce')%Js(1000.0)))
    var.put('nonceSec', var.get('Math').callprop('floor', (var.get('nonce')/Js(1000.0))))
    var.put('nonceRnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(65535))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(2.0)):
        try:
            var.get('counterBlock').put(var.get('i'), (PyJsBshift(var.get('nonceMs'),(var.get('i')*Js(8.0)))&Js(255)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(2.0)):
        try:
            var.get('counterBlock').put((var.get('i')+Js(2.0)), (PyJsBshift(var.get('nonceRnd'),(var.get('i')*Js(8.0)))&Js(255)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        try:
            var.get('counterBlock').put((var.get('i')+Js(4.0)), (PyJsBshift(var.get('nonceSec'),(var.get('i')*Js(8.0)))&Js(255)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('ctrTxt', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        try:
            var.put('ctrTxt', var.get('String').callprop('fromCharCode', var.get('counterBlock').get(var.get('i'))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('keySchedule', var.get('Aes').callprop('keyExpansion', var.get('key')))
    var.put('blockCount', var.get('Math').callprop('ceil', (var.get('plaintext').get('length')/var.get('blockSize'))))
    var.put('ciphertext', Js(''))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('blockCount')):
        try:
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('counterBlock').put((Js(15.0)-var.get('c')), (PyJsBshift(var.get('b'),(var.get('c')*Js(8.0)))&Js(255)))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('counterBlock').put(((Js(15.0)-var.get('c'))-Js(4.0)), PyJsBshift((var.get('b')/Js(4294967296)),(var.get('c')*Js(8.0))))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            var.put('cipherCntr', var.get('Aes').callprop('cipher', var.get('counterBlock'), var.get('keySchedule')))
            var.put('blockLength', (var.get('blockSize') if (var.get('b')<(var.get('blockCount')-Js(1.0))) else (((var.get('plaintext').get('length')-Js(1.0))%var.get('blockSize'))+Js(1.0))))
            var.put('cipherChar', var.get('Array').create(var.get('blockLength')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('blockLength')):
                try:
                    var.get('cipherChar').put(var.get('i'), (var.get('cipherCntr').get(var.get('i'))^var.get('plaintext').callprop('charCodeAt', ((var.get('b')*var.get('blockSize'))+var.get('i')))))
                    var.get('cipherChar').put(var.get('i'), var.get('String').callprop('fromCharCode', var.get('cipherChar').get(var.get('i'))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('ciphertext', var.get('cipherChar').callprop('join', Js('')), '+')
            if ((var.get('WorkerGlobalScope',throw=False).typeof()!=Js('undefined')) and var.get('self').instanceof(var.get('WorkerGlobalScope'))):
                if ((var.get('b')%Js(1000.0))==Js(0.0)):
                    var.get('self').callprop('postMessage', Js({'progress':(var.get('b')/var.get('blockCount'))}))
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    var.put('ciphertext', var.get('base64Encode')((var.get('ctrTxt')+var.get('ciphertext'))))
    return var.get('ciphertext')
PyJs_anonymous_10_._set_name('anonymous')
var.get('Aes').get('Ctr').put('encrypt', PyJs_anonymous_10_)
pass
@Js
def PyJs_anonymous_11_(ciphertext, password, nBits, this, arguments, var=var):
    var = Scope({'ciphertext':ciphertext, 'password':password, 'nBits':nBits, 'this':this, 'arguments':arguments}, var)
    var.registers(['blockSize', 'ctrTxt', 'counterBlock', 'b', 'c', 'ct', 'cipherCntr', 'plaintxtByte', 'ciphertext', 'password', 'key', 'nBits', 'pwBytes', 'i', 'plaintext', 'keySchedule', 'nBlocks', 'nBytes'])
    var.put('blockSize', Js(16.0))
    if (((var.get('nBits')==Js(128.0)) or (var.get('nBits')==Js(192.0))) or (var.get('nBits')==Js(256.0))).neg():
        PyJsTempException = JsToPyException(var.get('Error').create(Js('Key size is not 128 / 192 / 256')))
        raise PyJsTempException
    var.put('ciphertext', var.get('base64Decode')(var.get('ciphertext')))
    var.put('nBytes', (var.get('nBits')/Js(8.0)))
    var.put('pwBytes', var.get('Array').create(var.get('nBytes')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('nBytes')):
        try:
            var.get('pwBytes').put(var.get('i'), (var.get('password').callprop('charCodeAt', var.get('i')) if (var.get('i')<var.get('password').get('length')) else Js(0.0)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('key', var.get('Aes').callprop('cipher', var.get('pwBytes'), var.get('Aes').callprop('keyExpansion', var.get('pwBytes'))))
    var.put('key', var.get('key').callprop('concat', var.get('key').callprop('slice', Js(0.0), (var.get('nBytes')-Js(16.0)))))
    var.put('counterBlock', var.get('Array').create(Js(8.0)))
    var.put('ctrTxt', var.get('ciphertext').callprop('slice', Js(0.0), Js(8.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        try:
            var.get('counterBlock').put(var.get('i'), var.get('ctrTxt').callprop('charCodeAt', var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('keySchedule', var.get('Aes').callprop('keyExpansion', var.get('key')))
    var.put('nBlocks', var.get('Math').callprop('ceil', ((var.get('ciphertext').get('length')-Js(8.0))/var.get('blockSize'))))
    var.put('ct', var.get('Array').create(var.get('nBlocks')))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('nBlocks')):
        try:
            var.get('ct').put(var.get('b'), var.get('ciphertext').callprop('slice', (Js(8.0)+(var.get('b')*var.get('blockSize'))), ((Js(8.0)+(var.get('b')*var.get('blockSize')))+var.get('blockSize'))))
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    var.put('ciphertext', var.get('ct'))
    var.put('plaintext', Js(''))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('nBlocks')):
        try:
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('counterBlock').put((Js(15.0)-var.get('c')), (PyJsBshift(var.get('b'),(var.get('c')*Js(8.0)))&Js(255)))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('c', Js(0.0))
            while (var.get('c')<Js(4.0)):
                try:
                    var.get('counterBlock').put(((Js(15.0)-var.get('c'))-Js(4.0)), (PyJsBshift((((var.get('b')+Js(1.0))/Js(4294967296))-Js(1.0)),(var.get('c')*Js(8.0)))&Js(255)))
                finally:
                        (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            var.put('cipherCntr', var.get('Aes').callprop('cipher', var.get('counterBlock'), var.get('keySchedule')))
            var.put('plaintxtByte', var.get('Array').create(var.get('ciphertext').get(var.get('b')).get('length')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('ciphertext').get(var.get('b')).get('length')):
                try:
                    var.get('plaintxtByte').put(var.get('i'), (var.get('cipherCntr').get(var.get('i'))^var.get('ciphertext').get(var.get('b')).callprop('charCodeAt', var.get('i'))))
                    var.get('plaintxtByte').put(var.get('i'), var.get('String').callprop('fromCharCode', var.get('plaintxtByte').get(var.get('i'))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('plaintext', var.get('plaintxtByte').callprop('join', Js('')), '+')
            if ((var.get('WorkerGlobalScope',throw=False).typeof()!=Js('undefined')) and var.get('self').instanceof(var.get('WorkerGlobalScope'))):
                if ((var.get('b')%Js(1000.0))==Js(0.0)):
                    var.get('self').callprop('postMessage', Js({'progress':(var.get('b')/var.get('nBlocks'))}))
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    return var.get('plaintext')
PyJs_anonymous_11_._set_name('anonymous')
var.get('Aes').get('Ctr').put('decrypt', PyJs_anonymous_11_)
pass


# Add lib to the module scope
aes = var.to_python()