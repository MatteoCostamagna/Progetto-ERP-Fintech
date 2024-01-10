SELECT
    convert(bigint,[timestamp]) as timestamp,
    [Entry No_],
    [Posting Date],
    [Type],
    [Description],
    [Work Center No_],
    [Quantity],
    [Setup Time],
    [Run Time],
    [Stop Time],
    [Invoiced Quantity],
    [Output Quantity],
    [Scrap Quantity],
    [Operation No_]
FROM
    [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972]

WHERE 
    convert(bigint,[timestamp]) IN (108104,108105)
;