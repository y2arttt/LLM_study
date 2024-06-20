from sentence_transformers import SentenceTransformer, util
import numpy as np


embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

# Corpus with example sentences
corpus = ['나는 아침에 밥을 먹었다.',
          '나는 점심에 운동을 한다.',
          '나는 저녁에 책을 읽는다.',
          '나는 자정에 컴퓨터를 한다.',
          '나는 새벽에 잠을 잔다.']

corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)


# Query sentences:
queries = ['나는 점심에 조깅을 한다.']

# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
top_k = 5
for query in queries:
 query_embedding = embedder.encode(query, convert_to_tensor=True)
 cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
 cos_scores = cos_scores.cpu()


 #We use np.argpartition, to only partially sort the top_k results
 top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
 
 


 print("\n\n======================\n\n")
 print("Query:", query)
 print("\nTop 5 most similar sentences in corpus:")


 for idx in top_results[0:top_k]:
  print(corpus[idx].strip(), "(Score: %.4f)" % (cos_scores[idx]))