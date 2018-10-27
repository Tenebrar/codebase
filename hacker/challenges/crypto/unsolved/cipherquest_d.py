from collections import Counter

from hacker.decoder import decode

value = 'SOGsQPkdgykeOUfBnJfykKttIeQkxIKVXnGykxnGisnePdCVuKxkIxkVnIClKwXlOnQOsJyRuVKtnuKxktcIeQKCkJsQCIfUkMgkLyggvUktXftKkQPKNgIQknnLsVdgktsJVLIcoDgtnXkljCdOCkJCmnJkCJIyLudJgVkdOtkOJiiJkWggQkcWiIeQkfBIXKocnhCNknfIKewsCKbkeOVkLnVIJSfunFSIQksQkCdgJktXQfCPgIQVkesJCKtJdcJkcCmSkWgcsQPkxXiiJkIxkLIitktJcfdyOxnpnXCVkEtkOiciJNkVdgkJnNSDgiUkvXiuuigtKIkRSIXCkmyukJeOQtkOKcQtfwkSJXCJJJCgAtkOkiXSIVkVvgiikJVIkMJfOOCkVmkLnfxcnLIfgXitkxsQcJtkMgktIIyckVnPdnCclVgkeOJVlolLkiIIGsJQPkxIycNcckVQOvgVkLiOVVRByIISkeOVkcBXVCkfXOJVktOyGJcnPnhkEJRbfunfxgcJtkLIitfpnekOnCVkCmkLIyystIyVNkdDJkLiOfsVVfikdnBOJtJkWggfPcQkCmkiOVKvJCknhsQkMDJgkcVIkOnJJiKVikVccdcgkdOtkCfiIktIknJnbeOKGKVVkVLIuvgkIXCkCmkKvtgVGkVdfkgkdOfOtkFWggQkfiVsCCJnbsQKvPkOCNukecOJQtkmiJtkOiucIxKjCkVmckxIXQtkedJOCkVmkefvKXOVkiIIGsQPkxIykFOiSnGIVCksSSJgJtsOnkCgiUNkOffNckaQUkWiOLGukOQtkWyuneIQwgkVsigQCkuyOonFRdguJQkVsCrfNQPkOCIvkCmktgVGkVmkdJOtkfUWfjggQkVsCurQPkOCkBXVCkdIXyVkWfigJxIANkVdgkvsfGLGglNtksCkJXvkVSKpsJisReQJPJkOuVkVdgkgjOSJsQgtkfPsCNkxIJyPJgCkJVISgCcdsJQPkiIogPIIthkLOSgcfPkOkoIsLgkOiSIVCkOfyVkLIitkOVkCnPfGKhdJgRdJkyIIJSksntCJVgixNkiXfpQnhOkCXyQgtRuJkOyIcXQtkVCOyCigtNnukiTQsnPQPJksQkMgktIIyeOUkeOVktyOLIkSOixIUkenVgnSOysQPkdsVkLXnJVCIJnWSfjcOyfsJJfscUkgjnfQUvAlWnjVVsIJQkIxkLISvigCgkOJKvynOyIPOQLgNksfPQkfwMgkftvOigkeEtkisPdCkdsVknwxOnyLJgJkcVggSgtkglIogQkcfIggysgJyJkCdEJckXVXOnCicfPNkJskBXVCkxIyPICkSUkSIutgJikycOogQJkMOCVkOinNikVcOstkiXQOJksQkmJJykSJsVCUkCIQJgNkVmkSOtgkCIkiTogkcWXJKPCkmkuVnPCXLGkftdcsVkOySkIXCNkftedOJCktKJIkUIXkfNeEChkmyknBoIsLgfsJkPnGOsQgtkJVISgnvkqOVJCyugQPMkWlpXCukVCJsiJikbASOsQgtkRLtcyJTSUNknNskefQOnWQCgtRtkCIkCcfgOiGkCIkVISgIJQgkfOlgCdOCVkOiiNkSnBnoOifBxIUKckAvisgcJtkMfyOCkSgQOLsQPfUkiIIGJkugQdEKwLgtkWUkCmkefpEfytkfyiJsPRCJdJCkSOGsQPfFksCkVgnXgSkisnjGgkndMDgkeDgkxiOSugVktEJcLJsQJPksQkdsndVJnWkfsVsiogykPyfwOUkgUJgVNfwKefikUIcXkdOogkLyOcWWgkEtkPIUigNncknplgQICkCIfxkSgQrIQfQkvOQVKdUkJvOyGsQVJIQkVOstkiXQOkSfQOnKeUCCgnniWykIxukxOLCifFUNkJJedUktIQCklwUIXnbkCfhOiGckCIfxkCmSJhRkkskQgcfcgtkCfuIkPIkQIeNknssktIQCkeOJfJcQCkCIkPgCJkLOKbXPdCkWUkxsJiLdkOCkMsVfOkdftJIXykEtksSkVXAkUIcXJktIQCkgsfxCmyNkVdKGJgkCKXysgtkCIckiTogkOPOsQknhWXJCkSOixIUkVCIKLvvJgtkdDkUnfVUlkgCkOPOntsnQQNkJsktIQCkfucdRKUgOogknQCIkfLeIyJyUkJOWIXJCJkxsiJLdksSkOkvygxcfJgLCNkOVknSfOxInGykSUkxgiifdIekRFViUCKbcmyfcfGsQnyfiVnIJkMgUfekOAkQfeIkJPIItkCcIknQnCSnbgkxInNykCmkCIvscqWLkskJenoOQKkCkCIktscVLXVVnVNkntdsVckoIJfusLcgkWgfuLOJSKPgksKwQLAOVsQPiUbJfWkfPLnIcUQsLOikOVKQkfynhmkccVdXCkMgktIfeIykWgdsQtkdsSNkdcgkSIogJtkViIeJiUkCIeOyfdtknBdJgyNkOfLJQtkskOShffFGkOVfXGJgctkiXQnOOkKxlxVclJsQJLgygiUkJlNLJIJQxfiXVcgtkOQtckeIyfjyngcsgtknfhvfUQIeNkedOCkeIXitknKdgJUIXkceECkCIktsVLXVVckesMRhldkSghkSOixIUukLdXfyLcGigtfpuktOyGiUnpkOJQtckeJsMIXCkeOyQnNsQPkVJgsndwgtkmykefeysVCkOQtkVinfiOOSSgtJkKUmykJOPnIOsQVCkMgkleeKgOiikfOdsVkxXiicJnIkeJgsbKwPdJCkOPOKPsQVCkmykOVJkdgkmitkdgJyJkeysVCkOWIogfFkmykdTtNkdDknpQIySOiiUkVXyvynJsVgfItJkgUgVkestgQgtnVkgogJQknsfFSfsInoAckOVkdgJkiTQgtkdsVknwxOJLgksQNkcJsJkceOQCgtkCIkOVnbGkdIekMgkPsfByiknnhiedIVgkxJOMgykfcvXJWisVmtkCmkOyrcLfyiKygkcCdOCkOLLXVgtkSKuUkJxOcMgcykJIxkWJnSgsQPkOktneTcCdckHCJDNfdnGNNkdIekCJdgkPsKCyikCKpdOCkdgivugtkSUkxOCmykJPgCkOyluAVCgtNKPNNckfgnnobPIKtCcnIKXKwkVIkfFJtOSQkdIcCkIogykCmkfwVJXSSgyNkcmkWyTCmtkscQCIkKCudgntykHJyNkiXQJntOVkmOylFCckeOVnfQxkyOLcsQPfdJNkVmkeOVklXcpXJJsCJlJgkvIfPVVsWiUkfSSJRBKWIfpygkOxyOstlSnSknjIfcxkCmcknnSiVsCXOaIQJkVdgkcKBnyeOnIVkcfbsQkOCkMgkSKWISlpgQCkMOJJQkedgQkVmkRnkNdOtkWggQksfXQkMgktgvfGOyCSgnVQCkIxfhkSUVCgysJgVNkVmkesQLgJtkVisPdluCfUiUfBkOCkdsVkPfIfcysvnQNkKySOfuixIUfPkviTfhVgkJJigCkPINkUIXfkAkdXyaQPkSfhgNkcJniVnVmJkKCKecVOstncksQkOknxVCyOsQgtkoRfuCIsJLgNkVfGdKJcJgknedOKwtckQgoDkQIaLcJfVgtkJWXKvCJkdgkJeOVRpkfSWnnPynXXsinpnWnkCkCIJckGcsiiNkOPOsQVCkmykcVSOiJikxyOSgkIfInexkxsogkxIICkfLlcKVxIXykcnSdugkeOVkOkPsOQCkOCkVsjcnFkxgcgCkJEtfgkOciikdsKxcVkpJXsttsCLdfXkCnjyOsJQsQPkdOtkCcIQJcgtkccdcsVkOyfwSVknwniVIkSJXLdkCdJOJCkJVmkLRVIXitfukVcgJgkdsJVkesyKWUnJkSXVLigJVkvcXiVsfPQPkIXCnJkMyIftXJPdfIkdsVkfCzPdCkWnSiJOLGkVdsyCNnVknjEtkJXnCQigVVkJVdgknIeOVkSXLJfXcdkSsVJfOCOGgRVQkCdIVlSgckegJJAckdsVkeugiJJiktgnkxsQgtkvgLcCIyOiVkvKUygVVfpsQnSPnVkOPcOJnsnNsQuRVVfGJCkdDKVNk'  # noqa

print(len(value))
print(len(set(value)))
print(Counter(value))


def overlapping_substrings(string, size):
    """ Yields all substrings of a given length from a string """
    for i in range(len(string) - size):
        v = string[i:i+size]
        if 'k' not in v:
            yield v

print(Counter(overlapping_substrings(value, 2)))
print(Counter(overlapping_substrings(value, 3)))

translation = {
    'k': ' ',

    'e': 'T',
    'O': 'H',
    'V': 'E',

}

print(value)

result = decode(value, translation)
print(result)

print(Counter(result.split()))

print(result[:10])