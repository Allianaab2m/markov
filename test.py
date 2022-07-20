import MeCab
import unidic_lite

tagger = MeCab.Tagger()
sample_txt = "今元エイムズ民の有名な方がコンパスやるっていうツイートが流れてきたからリプ欄見たんやけど「垢買いしてどうにかする」とかって言っててそれを肯定してるような返答が入っててこれが地獄かと"
result = tagger.parse(sample_txt)
print(result)
