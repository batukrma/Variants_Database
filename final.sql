DELIMITER //

CREATE PROCEDURE GetVariantIdByGeneSymbol(IN geneSymbol VARCHAR(255))
BEGIN
    SELECT variant_impacts_gene.variant_id
    FROM variant_impacts_genes
    JOIN gene ON variant_impacts_gene.symbol = gene.symbol
    WHERE gene.symbol = geneSymbol;
END //
cancervariants
DELIMITER ;

call GetVariantIdByGeneSymbol("oca");



--

DELIMITER //

CREATE PROCEDURE GetVariantCountByGeneSymbol(IN geneSymbol VARCHAR(255), OUT variantCount INT)
BEGIN
    SELECT count(variant_impacts_gene.variant_id)
    INTO variantCount
	FROM variant_impacts_gene
	JOIN gene ON variant_impacts_gene.symbol = gene.symbol
	WHERE gene.symbol = geneSymbol;
END //

DELIMITER ;

select @totalCountOCA;
call GetVariantCountByGeneSymbol("oca", @totalCountOCA);

--


DELIMITER //

CREATE PROCEDURE GetDiseaseNameFromIdentifier(INOUT diseaseInput VARCHAR(255))
BEGIN
    select disease.disease_name
    into diseaseInput
	from disease
	where disease.identifier = diseaseInput;
END //

DELIMITER ;

set @diseaseInputOutput = "EFO_0004269\r";
call GetDiseaseNameFromIdentifier(@diseaseInputOutpu);
select @diseaseInputOutput;