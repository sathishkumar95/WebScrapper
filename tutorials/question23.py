with open('happynumbers.txt', 'r') as hp:
    with open('primenumbers.txt', 'r') as pm:
        hpline = hp.readline()
        pmline = pm.readline()
        hplst = []
        pmlst = []
        i=0
        while hpline and pmline:
            hplst.append(int(hpline))
            pmlst.append(int(pmline))

            hpline = hp.readline()
            pmline = pm.readline()

        overlap = [ele for ele in hplst if ele in pmlst]
        print(overlap)
