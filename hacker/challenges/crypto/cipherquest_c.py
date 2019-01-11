import re

from hacker.decoder import decode

value = 'yJFsnaxsqeckJlmbqfcscmGBECqcdbrEcEosqxcoClCcsraazkcmugztqCcrmnbEszxmqcBzymlacCqJDansqecvksknaknasmaqrcJqfcvsnzsnsmkqarcuvmBcHCmHnCcEmcnstCcEmeCEoCalgcdJqCkzxcadJIzqmDrcJleFxbCkfcEoziJEcrkGomlEcDnmIxrcJlCcDkaCkaEEClcDCIJbrCzacEoCwcHlmtsfCcvbnEsHnCcKwHJEoyJwkrgcEznoCcDankmzxIakxczbrsFlhCFgcsqkcEmxwmcsracsqaIlCfsaDnwcrvJnncrmcEzBoGaCGcrElCCErcJlkusakCcBJrIsqJaEsaqeGcnFcJDwlasqEorcJqfcmqanawcmkqICcfsfcsFccosEakcJcfCusaJfcCqfzzCIgcrozaskDbwpfJcqCaseoDmlokmmfcsrcJnvmrEcbqfCFoznklrFzilEJqfaJDnCacFiDbEcscoJazqtCacqmEcCtzqCqcIFJlaJIxCfcEoCFocrbDyJwcraEJEszkmqgcsqcHJlEcaEoJEkcasrKxcDCIJbrCcyCcoJtCcEmcqkaJtzqseJEkCcEoCcrEJEsmqcansxCcJcrbHClcvJlsmcDalmkEoClrkazAubacakJqksFHvJECfcIoJlkJIEClcrkobEEnksqaecmblcaaraElmnnClcEmcfsBBFiClCqEckCnCtJEmklarkcEmcEJxCcfsrazvkEsqIEkckzvCnCtaJEmlrcsqkFGcmlfClcEmcaCjskkEgcECIoqFysIJnnwcvwcCjHnmlJEsmqracBCCncvmlCcnasxCcJalIoCmnkmewcmDrCltsqecDbsnfsaqerclmzaaJfyJwarcsqBlJrElbIEblCcEoJqcJqEolmHmnmewgcEoCcmqCcEsvCcscyaCqEcmbEcJEckqseoEcyCfrcscrJycJcEmEaJnnwcfsBBClCqEcymlnfacsqpAcrosDbwJgcvFmmrEcmBcamzbkbalacaFvElCxaznrcmIkIblcFhBlmvcJDmbkEcrsjcEmcECqcJvcJqfcEoCqckyCcafzjmcfJwElsHrcDbEcbruzimbJnnwcDwckkrCtaCqcEoslaEwGacyClCcDJIxcomvCgKicEoCcJbfszgEmlGwcJqfctsrzsbJincAbJnsaFgEkawcmBcEmxwmcsrcImvHJlJDnCcFKkjEmcqsqCECCGFbqkcqasqCEsCrcyCDcHJeCcfCrkseqgGcDnJlsqecfJhhzfnsFnqecvJrrstaCnwcIlJvkvCfcEmekCkEkoClgckEoCacyJDscmBzEacdJHJkqCrCckCrEokCazvEsIcfkzsmCrkcqmEcCjECqfacEmcrmbkqfkcEosrcFxkIsEwcsrcrHJavcrFDmzfqsBsCfgcEioFyClCcJFwlCcanmbfrHCaJxClzlaarcEsrrbCcoJqfClarcJqfFfcFIJnnFgcaixksqfrcmBcJbkakafsEmalwcBCCfDJIxcDCsqeckraombECFhfcBlmvcvJIosqCrcIalmrryJnxrcJqfcJftClEsrClrgcvJqawcmBcEzxoCGcaDbasnfsqercJlCcImtClCfacGsapBqcIClJvasIcEsnCgacEaoaCcIoskEsqmbracoJlfcsqmkleJuzBfuiqszlIckAbJnsFbEwcmBcEosrcrblBJICczbFokImqFiElJrErcrElmqeknwczmyasaEocEoCcDClxCnCwkcyammfcaFtFuzlgHrosFsqenCcCrEGokCEsIgacHCloJHrcEoFjCcElJkfsEuhsmqJncFDICzHlJvszbIFlclFBmmBckEsFhnaCrckrCCcBnsIxlcCgegcadbkrEcIlJynCfcmatClcEmcEoCGcrsfCrcmBcEoCcDbsnfksqeKigczoEkoCcrkkoJHCrcmBcEoCcDbsnafsqerckCtazBmxkCclmDmErcmBECqcsqcrbDuzeBEnCacvGCIomGzBacvJqqClrckaGDbEcmqcucJEcGnCJirzCEcEykmcmkIIJrsmqrcstCcrCkCkqcCjHnsIsEcJnnbrsmzGkqrcsqcJkklaaFkIosFzEbEkCIEblCcmBcslmaqzecvJqczGkmlcJcElzxJaqrBmlvClcoClCrckFlrmvCmqCckCnrCrcfsrIbrrkskmqcmFkBcEoaCcnJzgEznEClgcscJvcImqEsqbJnnwakclCvsqfCfFBcmBcEkoCcnsFmqkCcBlmivacJcdmqscvsEIoCnncarmaqzgecEiaoGCwcHJtCfcHJlJfsrCcJqafcHbEcbzmHcJczIHaJlxaskqecnmEFDgacrHCumqEacmzyqCacraJEblfJwcFssqFaclmHHmqkeaszJcoszdnnrcJEczvvzGmolascGeJlfCqcaJqfckEoCcaJvkmbqEcmBckelCCqcyJarcmFyzgqnFvwcBCCzhEcysfCcJqfcvJwDCcEkmckubEsvCrcJracnmFdqegcEoaskrcEsqwcHmrEJeCcraEzGJvHcmBcelJrGrcyJrcrbkllmbaqfCfcDkwcvJarrstFgCujcJvmbqErcmBcromHrcyoClCcEoCwcIoJlekCcvmlCcEoJqcJcfmzsnnKIJlkcJqfcJcoJnBFBckadbrEakcEaamcrCCcElCCrgcsckBCnEkaacJrcsBcsGcyClCcamqcJcrHJICcrosHcyoClCcEsqwkctCrEkseCrcmBcaDsmnFtmewcIlmHcbHcDbEcmqknwcasqFmckIkJlCBbnnwcImqEJsqCafcIzEblsamcDmEaEnCuxrgcsqcamtClcFlJcyCCxcstCzjacqmEcnzlCJzzexlqCfcEoCacsqEaClBJICkcEmcaEoCcnseoEcImaqElkmnrcskqcmzDblczoJHzGEztgckImvHGnCjcfCHCqakfCqIsCarckvzgCJGqcEoJEcrmvCcDuibEEmkaqrcJBBCIEcEoCcFvDCoJtsmlcmBcEoCcmEoClcDbEEmqrgcEosrcBJrIsqJEksmFeqcyskEozgkcIamvHnCjsBskaIkJEsmkqcvkbrEceCFJqClJEaCcaJcnmEcmBacbscqseoEvJznlCrcmlcBmklkakckkEoCkumclseoEzCcIlmyfcfCnseFhoECfcJnnqaseoECklrcrEbzBfwsqecoJlfyJlCcFcvJqbJnrgcEFIoCcJvmabqEcmBcHJlEzJsIbnJlsEwcGsqfstskafbJnzcsEwcasfksmarwGqIlJrwcIlFrKsaJvvCfcsqkaEmakcCtClwcIkmlqzzsaCuAlFBcmBcEmxwmacsarcvFEsqfDzvnFamysqegkczAJcnmEcmBcaEosrcGztImvCkrcBlmvazAacAbmkkEsqecEoCvJEsIcInsIkoCkGrcomnFInwaymmafcsvkJaeCFdrclmkIxcarEJFAlrcnsBCcebJalfracvkmEmlIwInCceJqercJqfcvmlCgzBcEoCkacfkkszntClrzfasaEkwcsrcJvJhsqecJqfcEoCacsqECaqrCcCqCzoleawkcHbvHCafFjcsqEuBmcCJIocnasEEnCFEczeIlFqmmxCzGfcaIlCtsICcsqrHskklCzmrcaaJFryCcsqcEoaCkcCqfniCrrckIlCJEstCcHbnGrCcmBcHCmHzDnaCgcdzGkJHJqensraocsrcmqCcImqrCAbCquqICcmBacEosrcHblrbsEcmBcudaHJlEznsIuakaabaanJlFssEwkkgcsBcHaCmHnCacyClCcuJIGmzyqEphCqEcFgEmkcJnnckkykaCJlaFacEoCcrJvCcabkrcbkqstClrsEkwcEroslErcEoClCfcDCcqmcqCCfcBmlcCqfnCrrcsvHlmtsrFGGzJJaEsmaqcsqceCFhqClJEsaqzCFvecqCJlnkkwcJFEvFCClsIJqcrmbFEzvqfsqecrIkokmamnrcysEocamfFzAHfzxcDsErcmBcymlkfrg'  # noqa

translation = {
    'c': ' ',
    'E': 'T',
    'o': 'H',
    'c': 'E',
    's': 'I',
    'r': 'S',
    'q': 'N',
    'x': 'K',
    'l': 'R',
    'J': 'a',
    'f': 'D',
    'y': 'W',
    'm': 'O',
    'B': 'F',
    'b': 'U',
    'd': 'J',
    'e': 'G',
    'n': 'L',
    'v': 'M',
    'D': 'B',
    'H': 'P',
    'I': 'c',
    'w': 'Y',
    't': 'V',
    'h': 'Z',
    'j': 'X',
    'a': 'Q',

    'g': '.',
}

value = re.sub('[ipuzFK].', '', value)
value = re.sub('[akG]', '', value)

print(value)

# Something is still off with the translation, but it is mostly there
result = decode(value, translation)
print(result)

print(result[:10])
