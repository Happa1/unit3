# select count(*) from main.INHABITANT where INHABITANT.gender='Male'and INHABITANT.state='Friendly'
#
# select avg(gold), count(*), V.name from INHABITANT join VILLAGE V
# on V.villageid = INHABITANT.villageid group by V.name;
#
# select count(*) from main.ITEM where ITEM.item like "A%";
#
# select distinct job from INHABITANT;
#
# select * from main.INHABITANT, main.ITEM where ITEM.owner = INHABITANT.personid and INHABITANT.job='herbalist'
#
# select I.item from INHABITANT join main.ITEM I
# on I.owner = INHABITANT.personid where INHABITANT.job='Herbalist';