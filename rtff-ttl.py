import rdflib
from rdflib import Graph

path_to_file = "/media/manuel/Tesi/Datasets/dataset-15144/void.ttl"


'''
g = Graph()
g.parse(path_to_file)

query = """
SELECT DISTINCT ?c
WHERE {
    ?e a ?c
}"""

qres = g.query(query)
for row in qres:
    print(f"{row.c}")
'''

             
def parseTTL(path_to_file):

    print(path_to_file)

    file = open(path_to_file, "r", encoding="utf-8")

    #read all the prefix
    while True:
        line = file.readline()
        if "@prefix" not in line:
            break

    #read all the lines 

    classes = list()
    entities = list()
    properties = list()
    literals = list()


    last_subject = ""
    last_predicate = ""
    next_triple = 0     #0 triple of type (s p o), 1 triple of type (p o) , 2 triple of type (o)
    a=0

    while True:

        line = file.readline()

        if not line:
            break   

        #check if the line is empty (only \n in it)
        if line != "\n": 
            
            object = ""

            if next_triple == 0: 

                split = line.split(" ")

                last_subject = split[0]
                last_predicate = split[1]
                object = split[2]
            
            
            if next_triple == 1:

                i = 0
                while line[i] == " ":
                    i+=1

                #read the predicate
                j = i
                while line[j] != " ":
                    j+=1
                    
                last_predicate = line[i:j]

                #read the object
                object = line[j+1 : len(line)]

            if next_triple == 2:

                j = 0
                while line[j]==" ":
                    j+=1

                object = line[j+1 : len(line)]

            if ",\n" in object:
                next_triple = 2
            if ";\n" in object :
                next_triple = 1
            if ".\n" in object :
                next_triple = 0

            print(last_subject)
            print(last_predicate)
            print(object)
            print(next_triple)

            #categorize entities and classes

            if last_predicate == "a" or last_predicate == "rdfs:type" :
                entities.append(last_subject)
                if "." in object:
                    classes.append(object.strip(".\n"))    
                if ";" in object:
                    classes.append(object.strip(";\n"))
            
            #add property
            properties.append(last_predicate)

            #add literals
            if "\"" in object:
                if ".\n" in object:
                    literals.append(object.strip(".\n"))
                if ";\n" in object:
                    literals.append(object.strip(";\n"))
                if ",\n" in object:
                    literals.append(object.strip(";\n"))
            
            
    print("Entities:"+str(entities))
    print("Classes:"+str(classes))
    print("Properties:"+str(properties))
    print("Literals:"+str(literals))

    file.close()

files = [
    "/media/manuel/Tesi/Datasets/dataset-2210/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-2556/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-5364/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-5451/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-6046/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-8112/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-9298/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-9461/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10144/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10145/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10235/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10251/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10284/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10658/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10703/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10825/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10936/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-10959/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11022/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11024/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11035/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11099/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11167/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11191/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11238/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11247/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11263/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11285/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11322/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11360/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11401/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11511/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11611/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11625/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11631/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11655/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11689/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11709/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-11828/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12275/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12577/foaf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12720/foaf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12819/index.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12935/foaf-momus.rdf",
    "/media/manuel/Tesi/Datasets/dataset-12989/aigp-dblp-sameas.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13043/foaf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13109/foaf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13152/doap.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13357/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-13357/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13357/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-13357/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-13378/wordsense-entity-noun-1.nt",
    "/media/manuel/Tesi/Datasets/dataset-13388/paris.nt",
    "/media/manuel/Tesi/Datasets/dataset-13412/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-13412/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13412/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-13412/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-13469/interpro-ipr000100.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/lemonentriespointingtosinglefile.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/individualspointingtosinglefile.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/lemonentriespointingtobigfile.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/simpleentries.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/simpleontology.nt",
    "/media/manuel/Tesi/Datasets/dataset-13577/individualspointingtobigfile.nt",
    "/media/manuel/Tesi/Datasets/dataset-13583/gold-2010.owl",
    "/media/manuel/Tesi/Datasets/dataset-13759/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-13759/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13759/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-13759/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-13796/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-13796/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-13796/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-13796/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-14079/mapping-eat-dbpedia.rdf",
    "/media/manuel/Tesi/Datasets/dataset-14080/33383.ttl",
    "/media/manuel/Tesi/Datasets/dataset-14195/nomisma.ttl",
    "/media/manuel/Tesi/Datasets/dataset-14198/data-and-taxonomy.ttl",
    "/media/manuel/Tesi/Datasets/dataset-14252/wordsense-entity-noun-1.nt",
    "/media/manuel/Tesi/Datasets/dataset-14472/bio2rdf-ndc-sio-mapping.owl",
    "/media/manuel/Tesi/Datasets/dataset-14603/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-14603/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-14603/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-14603/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-14806/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-14806/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-14806/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-14806/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-14821/gold-2010.owl",
    "/media/manuel/Tesi/Datasets/dataset-14921/lemonentriespointingtosinglefile.nt",
    "/media/manuel/Tesi/Datasets/dataset-14921/individualspointingtosinglefile.nt",
    "/media/manuel/Tesi/Datasets/dataset-14921/lemonentriespointingtobigfile.nt",
    "/media/manuel/Tesi/Datasets/dataset-14921/simpleentries.nt",
    "/media/manuel/Tesi/Datasets/dataset-14921/simpleontology.nt",
    "/media/manuel/Tesi/Datasets/dataset-14921/individualspointingtobigfile.nt",
    "/media/manuel/Tesi/Datasets/dataset-15082/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-15082/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-15082/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-15082/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-15144/void.ttl",
    "/media/manuel/Tesi/Datasets/dataset-15150/owl.owl",
    "/media/manuel/Tesi/Datasets/dataset-15150/rdf-schema.rdf",
    "/media/manuel/Tesi/Datasets/dataset-15150/contact.nt",
    "/media/manuel/Tesi/Datasets/dataset-15150/22-rdf-syntax-ns.nt",
    "/media/manuel/Tesi/Datasets/dataset-15414/paris.nt",
    "/media/manuel/Tesi/Datasets/dataset-15633/applications-by-account.nt",
    "/media/manuel/Tesi/Datasets/dataset-15658/ccwater-organogram-30-sept-2011.rdf",
    "/media/manuel/Tesi/Datasets/dataset-15803/dfe-20data-20september-202011.rdf",
    "/media/manuel/Tesi/Datasets/dataset-15976/ingresos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15976/gastosfuncionales.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15976/gastos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15977/ingresos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15977/gastosfuncionales.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15977/gastos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15978/ingresos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15978/gastosfuncionales.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-15978/gastos.jsonld",
    "/media/manuel/Tesi/Datasets/dataset-16034/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16035/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16036/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16037/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16038/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16039/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16040/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16041/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16042/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16043/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16044/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16045/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16046/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16047/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16048/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16049/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16050/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16051/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16052/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16053/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16054/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16055/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16056/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16057/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16058/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16059/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16060/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16061/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16062/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16063/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16064/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16065/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16066/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16067/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16068/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16069/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16070/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16072/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16073/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16074/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16075/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16076/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-16077/ore-rem.ttl",
    "/media/manuel/Tesi/Datasets/dataset-17283/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-17375/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-17913/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-17925/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-19019/rows.rdf",
    "/media/manuel/Tesi/Datasets/dataset-21682/mf-portfif-2-th-12.rdf",
    "/media/manuel/Tesi/Datasets/dataset-21683/mf-portfif-1-th-12.rdf",
    "/media/manuel/Tesi/Datasets/dataset-21685/mf-regis-th-12.rdf",
    "/media/manuel/Tesi/Datasets/dataset-24154/tbgy-vw5z.rdf",
    "/media/manuel/Tesi/Datasets/dataset-29412/kc9i-wq85.rdf",
    "/media/manuel/Tesi/Datasets/dataset-29436/cnfp-tsxc.rdf",
    "/media/manuel/Tesi/Datasets/dataset-29783/qizy-d2wf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-31118/ukv7-jfmv.rdf",
    "/media/manuel/Tesi/Datasets/dataset-31599/54yg-8jz5.rdf",
    "/media/manuel/Tesi/Datasets/dataset-38134/2er7-i3zj.rdf",
    "/media/manuel/Tesi/Datasets/dataset-39483/adzi-ting.rdf",
    "/media/manuel/Tesi/Datasets/dataset-39531/e5vi-a3tx.rdf",
    "/media/manuel/Tesi/Datasets/dataset-39552/3ukt-87ju.rdf",
    "/media/manuel/Tesi/Datasets/dataset-40758/wrpp-is68.rdf",
    "/media/manuel/Tesi/Datasets/dataset-40908/xfij-5ugz.rdf",
    "/media/manuel/Tesi/Datasets/dataset-41134/e4mh-a2u3.rdf",
    "/media/manuel/Tesi/Datasets/dataset-41151/ty3c-qr7r.rdf",
    "/media/manuel/Tesi/Datasets/dataset-43154/3e5s-3q2t.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44016/6x9d-idz4.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44051/cf7e-dhrb.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44088/tzak-8e66.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44849/h9vb-3tcy.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44859/ng43-255b.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44871/ud3j-i2ws.rdf",
    "/media/manuel/Tesi/Datasets/dataset-44877/f2q7-6uiv.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45524/w4sk-nq57.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45526/tvq9-ec9w.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45529/hz9m-tj6z.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45553/vqqm-nsqg.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45604/jhsu-2pka.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45627/5aye-4rtt.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45806/nen9-84ke.rdf",
    "/media/manuel/Tesi/Datasets/dataset-45815/nhy6-gqam.rdf",
    "/media/manuel/Tesi/Datasets/dataset-46447/xr9u-qg7n.rdf",
    "/media/manuel/Tesi/Datasets/dataset-46542/ajtb-tms2.rdf",
    "/media/manuel/Tesi/Datasets/dataset-47505/fjs5-35cn.rdf",
    "/media/manuel/Tesi/Datasets/dataset-47562/r6vz-x6jf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-51693/gpn8-sbpq.rdf",
    "/media/manuel/Tesi/Datasets/dataset-51718/3gkq-ags9.rdf",
    "/media/manuel/Tesi/Datasets/dataset-51786/w9kt-3hk8.rdf",
    "/media/manuel/Tesi/Datasets/dataset-51895/rpzm-6wvf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-51932/rgq9-zjqv.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52511/dszh-kvzr.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52562/wq8k-pnqg.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52591/dscg-f8mh.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52690/ncz3-ptfk.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52743/nwdp-pxq4.rdf",
    "/media/manuel/Tesi/Datasets/dataset-52856/yay2-kfah.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54958/hqa9-fu65.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54959/26n4-t3i2.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54960/bxas-tthn.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54961/e5yz-rhka.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54962/qqc4-zyw5.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54963/ncb4-kvyy.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54964/2nt5-t4gz.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54965/jm5p-4tih.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54966/e46j-f6vr.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54967/33c2-vvwz.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54968/bcmx-n3c4.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54969/xay3-emkq.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54970/aa8h-5r4x.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54971/bn76-emh9.rdf",
    "/media/manuel/Tesi/Datasets/dataset-54972/w5r2-3t5j.rdf",
    "/media/manuel/Tesi/Datasets/dataset-63637/mdmf-aswt.rdf",
    "/media/manuel/Tesi/Datasets/dataset-63805/giq8-gspk.rdf",
    "/media/manuel/Tesi/Datasets/dataset-63944/c34u-vnew.rdf",
    "/media/manuel/Tesi/Datasets/dataset-63951/d83j-k75n.rdf",
    "/media/manuel/Tesi/Datasets/dataset-63958/szs6-ihk8.rdf",
    "/media/manuel/Tesi/Datasets/dataset-64225/bhrt-29rb.rdf",
    "/media/manuel/Tesi/Datasets/dataset-65708/myju-bx58.rdf",
    "/media/manuel/Tesi/Datasets/dataset-65952/snxs-8atp.rdf",
    "/media/manuel/Tesi/Datasets/dataset-66005/2ynm-erms.rdf",
    "/media/manuel/Tesi/Datasets/dataset-66165/khtu-ck6k.rdf",
    "/media/manuel/Tesi/Datasets/dataset-66467/tb7s-6pqn.rdf",
    "/media/manuel/Tesi/Datasets/dataset-68298/2qji-4zqf.rdf",
    "/media/manuel/Tesi/Datasets/dataset-68732/vsbg-t3e9.rdf",
    "/media/manuel/Tesi/Datasets/dataset-73786/3wtr-89us.rdf",
    "/media/manuel/Tesi/Datasets/dataset-75678/j55h-3upk.rdf",
    "/media/manuel/Tesi/Datasets/dataset-76281/hv9n-xgy4.rdf",
    "/media/manuel/Tesi/Datasets/dataset-77345/8qjh-sbs9.rdf",
    "/media/manuel/Tesi/Datasets/dataset-80848/r6sk-x3g9.rdf",
    "/media/manuel/Tesi/Datasets/dataset-88131/v9dk-xgzr.rdf",
]

parseTTL(path_to_file)
                
            
            



    

