# STL10 - Segmentation

Please consider sponsoring this repo so that we can continue to develop high-quality datasets for the AI and ML research.

To become a sponsor:

[GitHub Sponsors](https://github.com/sponsors/semihyagli) <br/>
[Buy me a coffee](https://buymeacoffee.com/semihyagli) <br/>

You can also sponsor us by downloading our free application, **_Etiqueta_**, to your devices:

[Etiqueta on iOS or Apple Chip Macs](https://apps.apple.com/us/app/etiqueta/id6504646776) <br/>
[Etiqueta on Android](https://play.google.com/store/apps/details?id=com.aidatalabel.etiqueta) <br/>


This repo contains segmented images for the labeled part of the [STL-10 Dataset](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://cs.stanford.edu/~acoates/stl10/&ved=2ahUKEwidyq31o9-LAxUQbvUHHeAOIx0QFnoECAgQAQ&usg=AOvVaw1TdzbOwKAoAz_-kLc5rghT).  <br/>
More information on the original STL-10 dataset can be found here: https://cs.stanford.edu/~acoates/stl10/ <br/>
Thanks to Martin Tutek, the original STL-10 dataset can be downloaded via the python code here: https://github.com/mttk/STL10


If you use this dataset in your research please do not forget to cite: <br/>

```
@techreport{yagli2025etiqueta,
  author      = {Semih Yagli},
  title       = {Etiqueta: AI-Aided, Gamified Data Labeling to Label and Segment Data},
  year        = {2025},
  number      = {TR-2025-0001},
  address     = {NJ, USA},
  month       = Apr.,
  url         = {https://www.aidatalabel.com/technical_reports/aidatalabel_tr_2025_0001.pdf},
  institution = {AI Data Label},
}
```
```
@inproceedings{coates2011analysis,
  title     = {An analysis of single-layer networks in unsupervised feature learning},
  author    = {Coates, Adam and Ng, Andrew and Lee, Honglak},
  booktitle = {Proceedings of the fourteenth international conference on artificial intelligence and statistics},
  pages     = {215--223},
  year      = {2011},
  organization={JMLR Workshop and Conference Proceedings}
}
```

Note: If you notice any errors and/or if you have comments/ideas relevant to this dataset or Etiqueta in general, please reach me out at [contact@aidatalabel.com](mailto:contact@aidatalabel.com).


Class | airplane | bird | car | cat | deer | 
--- | --- | --- | --- | --- | --- |
original  | ![airplane](examples/original_airplane_4599.png) | ![bird](examples/original_bird_2297.png) | ![car](examples/original_car_2606.png) | ![cat](examples/original_cat_546.png) | ![deer](examples/original_deer_3472.png) | 
segmented | ![airplane](examples/segmented_airplane_4599.png) | ![bird](examples/segmented_bird_2297.png) | ![car](examples/segmented_car_2606.png) | ![cat](examples/segmented_cat_546.png) | ![deer](examples/segmented_deer_3472.png) | 

Class | dog | horse | monkey | ship | truck | 
--- | --- | --- | --- | --- | --- |
original  | ![dog](examples/original_dog_2537.png ) | ![horse](examples/original_horse_6056.png)  | ![monkey](examples/original_monkey_2987.png) | ![ship](examples/original_ship_1628.png) | ![truck](examples/original_truck_2999.png) | 
segmented | ![dog](examples/segmented_dog_2537.png) | ![horse](examples/segmented_horse_6056.png) | ![monkey](examples/segmented_monkey_2987.png) | ![ship](examples/segmented_ship_1628.png) | ![truck](examples/segmented_truck_2999.png) | 


### Notes: 
We have caught the following errors in the test part of the STL-10 dataset: <br/>

'1495' 'cat_0' mark is in fact a 'dog_0'. <br/>
'6417' 'cat_0' mark is in fact a 'dog_0'. <br/>
'1718' 'cat_1' mark is in fact a 'dog_0'. <br/>
'1138' 'dog_1' mark is in fact a 'cat_0'. <br/>
'1484' 'dog_1', 'dog_2', 'dog_3' are in fact 'sheep_0', 'sheep_1', 'sheep_2'. <br/>
'6566' 'dog_0' and 'dog_1' marks are in fact 'cat_0', and 'dog_0'. <br/>
'7902' 'dog_0' and 'dog_1' marks are in fact 'cat_0', and 'dog_0'. <br/>