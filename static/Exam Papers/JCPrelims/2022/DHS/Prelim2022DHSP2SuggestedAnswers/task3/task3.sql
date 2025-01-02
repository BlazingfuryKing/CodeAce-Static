select ballot_result,group_id from Results where nric='T0663758C';


select names, ballot_result from Results, Names on Results.nric = Names.nric where (Results.group_id=(select group_id from Results where Results.nric='S9981511E') and Results.nric<>'S9981511E')
