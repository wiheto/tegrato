# Changelog

## Version 0.5.2 (In development)

### 0.5.2 Improvements

Improved sidecar checking.

Added is_jsonable to utils.

### 0.5.2 Fixes

Fixes the issues when shortest paths were trying to be derived on non existent time points (raised in #60)

Fixing problem with df_to_array when time indices do not start at 0.

Fixing problem with dataframe netshape when starttime !=0 (#61)

coveralls resynced with travis (pip install python-coveralls replaced with pip install coveralls)

### 0.5.2 Changes

Removing wrong cased variables (e.g. netIN and TN from utils)

## Version 0.5.1

### 0.5.1 Improvements

Better what is temporal network tutorial

censor_timepoints documentation is clearer.

### 0.5.1 Changes

Changing raiseIfU variable to rasie_if_undirected in check_input

### 0.5.1 Fixes

Updated requirements and fixed outdated version of scipy being installed on clean install using pip. 

Fixed header bug in documentation

Fixed that TenetoBIDS bids_filter dicts only contain sub,ses,task and run after calling tnet.run().

Updated remove_confounds documentation to fit with new TenetoBIDS

Allows param dicts in TenetoBIDS functions to be numpyarray by converting input to JSON (fixes #62)

## Version 0.5

### 0.5.0 Improvements

Changing argument names in network measures to 'pertime' and 'overtime' replacing 'time' and 'global' to be clearer.

More detailed documentation to temporal_degree_centrality.

More detailed documentation to temporal_closeness_centrality.

Changing argument values for minimize in shortest_temporal_paths, it is now called: 'temporal_distance' instead of time.

Single instance of version specified in teneto/_version.py.

Output format can be specified in binarize,

TenetoBIDS rewritten. Compatible now with pybids. Easier to use.

censor_timepoints and exclude_runs now in bidsutils as functions (and streamlined) instead of in TenetoBIDS.

### 0.5.0 Changes

Python 3.6 is now required.

Scipy requirements updated.

Tougher coding standards implemented through prospector

Renaming getDistanceFunction to get_distance_function.

Created `teneto.neuroimagingtools` to contains neuroimaging specific functions.

fmriutils and bidsutils have moved to neuroimagingtools.

Changed distance_func_name to distance_func in volatility.

Instantaneous phase synchrony is now between 0 and 1, fixing potential wrapping issue.

### 0.5.0 Fixes

Betweenness centrality now normalizes across time with sigma_jk.

Fix error in #53.

Binarize can accept dataframe in sparse.

Remove_confounds can deal with dataframes.

Fixing inclusion of testdata/dummybids when installing with pip.

## V0.4.6

### 0.4.6 Enhancements

Asarray flag in get_network_when returns dense version of network.

Adding CustomBIDS to derivative description json file in TenetoBIDS.

Added deprecation warning to TenetoBIDS

Better docs

Renaming temporalcommunity to communitymeasures for clarity/consistency

teneto.io added

readthedocs.yaml added

### 0.4.6 Fixes

Fixing case where, for array input, get_network_when with directed edges dropped duplicates.

Fixed missing bracket in get_network_when (credit to: lcandeago #45)

## V0.4.5

### 0.4.5 Enhancements

Added teneto.TenetoWorkflows (name may change to just workflows)

Added promiscuity and persitence to temporalcommunity measures

Updating to fmriprep 1.4.0 updated BIDS naming conventions. fmriprep&lt;1.4.0 no longer compatible.

make_parcellation now uses templateflow and all atlases therein

save_tenetobids_snapshot to export current teneto settings. save_to_pickle (and corresponding load function) have been removed as they are not secure.

### 0.4.5 Fixes

NaNs in allegiance, which fixes recruitment and integration. Also added squeeze to input. And bug in integration where for loop would generate error.

Removed self from teneto history.

Some minor TenetoBIDS fixes

### 0.4.5 Changes

Removing unused description_string function from bidsutils

Renaming of dummybids data

Placing custom BIDS formatting in external json config folder.

Removing seaborn as requirement (unused)

Removing function load_parcellation_coords

Removing call to eval and instead getattr in tapered windowed method in genereate_temporalnetwork.

Params for distribution in tapered window method in genereate_temporalnetwork should now be a dictionary not a list.

## V0.4.4

Schaefer 7 network communities now reference the packaged image (17network mask). Before they references the 7 network mask that was not included.

Added plotedgeweight option to sliceplot for varying edge size.

Minor fixed to TenetoBIDS, teneto.timeseries and teneto.communitydetection

Adding export_history to TenetoBIDS.

Divide resolution of louvain by number of time-points (so gamma is relative to each snapshot)

Default of consensus matrix in community detection set to 0.5.

Changed make_parcellation to accept +OH (for subcortical) and +SUIT (for cerebellar)

Fixed error where tags are set and other folders exist in derivatives

Renaming Schaefer atlas files

Adding Scahefer atlas to data/parcellation_defaults/default.json

Better loading of communities in TenetoBIDS

Renmaed network_communities_ to communitytemplate\_

Fixed a bug where SUIT and OH were not loaded in make_parcellation

Better communitytemplate\_ tables loaded (OH and SUIT included)

Can specify 7 or 17 communitytemplate size when using schaefer atlas

Allow to apply thresholding within bursty_coeff function

Fixed flexibility inversion bug (values were previously reversed)

Added tctc.

Dataset_description.json added to teneto pipeline in derivatives (TenetoBIDS)

pybids always imported in TenetoBIDS (but validator turned off)

dataset_description exported with export_history (as tenetoinfo.json)

fixing exclusion confound when criteria is based on SD (previously an error was raised)

Added dense compatibility to TemporalNetwork and get_network_when

Added instantaneous phase

Fixing speed problems for temporal network!

Fixing issue in within community estimates for bursty_coef when calc='communities'

## V0.4.3

Added Schaefer atlas

Added SUIT atlas

Fixed error in temporal_louvain/consensus matrix where labels were getting incorrectly sorted.

Adding temporalcommunity module.

Adding flexibility to temporalcommunity

Removing tenetoBIDS.load_community_data()

Adding communities option to load_data.

Fix to TenetoBIDS.get_pipeline_subdir_alternatives

Removing 'csv' loading from TenetoBIDS (should be tsv)

Fix for nodekwargs{'c'} specification in graphlet slice plot. (Fixes #18)

## V0.4.2

Fixed a bug in load data of TenetoBIDS when loading networkmeasures from multiple subjects (error was thrown).

Document updates in teneto.timeseries

Fixed a bug in TenetoBIDS confound loading where index_col was first confound.

Making dimord consistency throughout TenetoBIDS (time,node) -> this may change.

Make ijt to be int in process_input from TemporalNetwork (assumes all timestamps are discrete and these are accounted for with metadata (sampling rate and timestart))

Fixed bug in TenetoBIDS's temporal community detection where dataframe was passed instead of TemporalNetwork

TemporalNetwork.N and TemporalNetwork.T forced to be integers.

Improved code quality.

Codacy checks added.

## V0.4.1

More documentation

Contributers page added in docs

temporal_part_coef renamed to temporal_participation_coeff

added: generatenetwork.rand_poisson

small fixes to tenetoBIDS

matplotlib kwargs added to slice_plot scatter and line parts

added hdf5 possibility to TemporalNetwork

Added utils.io for networkx export of a snapshot.

Renamed teneto.derive package to teneto.timeseries

Renamed teneto.derive.derive to teneto.timeseries.derive_temporalnetwork

Renamed teneto.TenetoBIDS.derive to teneto.TenetoBIDS.derive_temporalnetwork

Rewritten participation coefficient. Fixed potential bug.

Added python-louvain dependency

Added temporal network louvain clustering

teneto.communitydetection imported when importing teneto

allow 2d arrays to be imported into temporalnetwork object

fixed transpose bug in TenetoBIDS makeparcellation when removeconfounds=True

mintor general improvements to TenetoBIDS.removeconfounds

Not yet compatible with HDF5-compatible:, temporal_degree_centrality, volatility, fluctuability, sid, topological overlap, and participation coefficient with negative edges)

## V0.4.0

Rewritten tenetobids to make more compatible with BIDS derivatives RC1 (note completely compatible yet).

Fixed relative import paths

Subnet argument for certain functions have been removed.

Changing default value of decay argument (temporal_degree_centrality, sid) to 0 instead of None

topological_overlap added to networkmeasures.

documentation improvements.

renamed net variable to tnet in networkmeasures.

added local_variation to networkmeasures.

added TemporalNetwork class.

Added randomseed to binomial.

Fixed layering of edges in circleplot

Fixed error in intercontacttimes where preset network was node,time not node,node

Rewritten intercontacttimes to be calculated through TemporalNetwork class' df-list instead of array.

Rewritten (partially) temporal_degree_centrality to be calculated through TemporalNetwork class' df-list instead of array. (communities still use array)

nLabs arugment changed to nodelabels

tLabs argument changed to timelabels

unit argument changed to timeunit

added cmap to circle_plot

rewritten shortest temporal paths. Now outputs pandas dataframe.

temporal_betweenness_centrality added.

## V0.3.5

Due to problems with installation of iGraph, temporarily removing communitydetection (commenting out code in TenetoBIDS, communitydetection module is not imported and tests commented.) This is until a more user friendly louvain detection is implemented (and is quick).

## V0.3.4

Removing **main**.py and some misc files not used

Added check to TenetoBIDS.load_community_data() for file to exist

Added missing warnings import in networkmeasures

Added more TenetoBIDS functions that use \_load_data

Correct caclulation of within-volatility when calc=communities

Changed file_hdr and file_idx in \_load_data

Improved matching of confound files and file in TenetoBIDS

Fixed bug for confound reports when windowed method used in TenetoBIDS.derive.

Added analysis tag to directory name of derive vs confound directory. Fixed paths to be absolute image links in html report

BIDS_dir is made to abspath in **init** of TenetoBIDS

Fixed bug where subjects couldn't be set in **init** of TenetoBIDS

Allowed ability to reload teneto_bids object when loading from pickle (for development purposes as some information (e.g. history) is lost)

Added communitydetection to TenetoBIDS

Added load_community_data to TenetoBIDS

communitydetection.temporal_louvain_with_consensus can be passed a 2d

Several minor improvements to exclusion_files and exclusion_timepoint in TenetoBIDS

Added TenetoBIDS.load_timelocked_data

TenetoBIDS.make_timelocked_events can now also do raw tvc

Added wait to concurrent.

Fixed bug. derive's loading of FC in JC weighting.

Improved tags in TenetoBIDS when loading data.

Improved timepoint exlcusion and bad_file continuity.

If timepoint exlcusion is spline, now the first and last time-point are not naned.

Added event related displacement (option in networkmeasures.volatility)

Added variable community number per time point compatibility for teneto.networkmeasures.sid and tnet.networkmeasures.temporal_degree_centrality

Other minor selection/load imprvement of tenetoBIDS.

removezeros option added to teneto.networkmeasures.temporal_part_coef

Fixed bug in decay in teneto.networkmeasures.temporal_degree_centrality

Added dummy bids test set to data

Fixed set task and set run bug when raw_data_exists is false.

Added graphlet based thresholding.

## V0.3.3

Added txt file generation to `temporal_exclusion_criteria` saying how many time-points are deleted.

rename temporal_exclusion_criteria and file_exclusion_critiera to 'set_timepoint_exclusion' and 'set_file_exclusion'

better importing of modules.

more numpydoc-ing of comments

improved tenetoBIDS.get_selected_files with respect to last_analysis_step

added tenetoBIDS.removeconfounds as standalone function that can still be called through tenetoBIDS.make_parcellation

added a tenetoBIDS.\_load_files() function to unity io code and increase compatibility through the different funcitons/file formats. However not implemented in all functions yet.

Allow to suppress confound report

## V0.3.2

Added a temporal participation coefficient to networkmeasures (`teneto.networkmeasures.temporal_part_coef`)

Allow contact representation in louvain clustering.

Started adding communities argument to replace subnet argument in networkmeasures.

Added DeprecationWarning for removal of subnet argument in Teneto 0.3.5

Added networkmeasures.temporal_part_coef and module_degree_zscore option in teneto.networkmeasures.temporal_degree_centrality.

Added `file_exclusion_criteria` and `temporal_exclusion_criteria` to TenetoBIDS

Updated confound_files selection in TenetoBIDS

## V0.3.1

**main** added (this may be removed at later date as I don't have an interest in maintaining this).

Added `njobs` argument to `TenetoBIDS` (and various other functions therein) for parallel computing.

added nilearn.signal.clean for denoising

removed statsmodels as dependence.

## V0.3.0

Dockerfile added

Added weight-var and weight-mean options to jackknife correlation.

Added make_static_connectivity in TenetoBIDS

Added from-subject-fc open to jackknife correlation in TenetoBIDS.derive.

Numpydoc adopted in docstrings (teneto.utils, teneto.generatenetwork).

Added `bad_subjects` and `set_bad_subjects()` in `TenetoBIDS`

Added readthedocs and pypi badge

Fixed `teneto.networkmeasures.volatility` when subnet is given.

Changed argument subnet_id in `teneto.networkmeasures.volatility` to subnet.

Added possibility to append OH subcortical atlas to make_parcellation.

Added tag option to TenetoBIDS

Changed cfg variable name to params in teneto.utils.

Fixed bug in teneto_degree_centrality where decay and subnet set.

Allow \* and + in tag in TenetoBIDS.

clean_community_indexes works with temporal clustering

Added iGraph as requirement

Added `teneto.communitydetection.louvain`

## V0.2.7

Added calc option to `TenetoBIDS.make_time_locked_events` allowing for selecting one of multiple networkmeasures

Corrected bug where timelocked files were not placed in timelocked directory

Changed all forms of time_locked and event-locked to timelocked

Added `load_parcellation_data` to `TenetoBIDS`

Added history to TenetoBIDS

Added install_requires to `setup.py`

## V0.2.6 (and partly V0.2.5)

Removed older examples.

Added functionality for  derivative only BIDS folders (ie if no raw data is present).

Added load/save TenetoBIDS object

Added bids to requirements.txt

Added dependency to seaborn (adde to requirements.txt)

Added confound reports to TenetoBIDS.derive

Added draft version of teneto/bids documentation.

Added Gordon2014_333 parcellation

Renamed parcellations to \[firstauthor]\[publicationyear]\_\[numberofrois]

Added more documentation to functions

Added `networkmeasures.sid`

Added forced division by 2 for within (calc: time and subnetwork specified)

Added version number to pipeline name in tenetoBIDS

Added `TenetoBIDS.make_time_locked_events` and `TenetoBIDS.load_network_measure`

Added `teneto.utils.get_dimord`

Fixed the `teneto.__version__` that wasn't getting updated (stuck on 0.2.2 for previous versions. So check setup.py in previous versions to be sure what version you were using.)

Updated readthedocs (fixed bugs)

Fixed pybids (instead of bids) in requirements. Removed unnecessary requirements

## V0.2.4b

Reverted back the incorrect fix for #1, added

Added distutils version to requirements.

## V0.2.4

Fixed `bursty_coeff` when ICT is empty.

Fix for #1

## V0.2.3

Added `confound_pipeline` option to TenetoBIDS.

Added nan-to-median for nans in confounds in removal in `TenetoBIDS.make_parcellation`

made `TenetoBIDS.networkmeasures` functional (i.e. saving files, removing an error).

replaced function `betai` with `betainc` for scipy 1.0 compatibility.

## V0.2.2

Corrected vminmax error in `plot.graphlet_stack_plot` when specifying a string.

Changed the default of vminmax in `plot.graphlet_stack_plot` to minmax

Fixed documentation error in vminma in `plot.graphlet_stack_plot`

Correct cmap bug in `plot.slice_plot`

Added `utils.load_parcellation`

Folder ./data is also included with teneto, at the moment shen2013_tal parcellation is included there. (This is currently under development). And may change name to specify that this has to do with brain research.

Added decay parameter to degree_centrality

Added additional names to 'multiple temporal derivative' method

corrected bug in `bursty_coeff` when specifying `nodes='all'` (previously an error was raised).

Added `utils.binarize` wiith 'binarize_rdp', 'binarize_percent', and 'binarize_rdp' as options

Added a inputtype item in netinfo dictionary returned by `utils.process_input`

Modified `utils.contact2graphlet` to ignore an empty nLabs list.

Added `utils.create_traj_ranges`

Added the module `trajectory` with `rdp` compression.

Added subnet argument to `networkmeasures.bursty_coeff` so that B is calculated per module.

Changed default of `params['report']` in `derive.derive` to 'no'

Added `params['report_path']` to `derive.derive`.

Corrected default dimension order of `derive.derive` to  'node,time'

Made report_name parameter to `derive.report.gen_report()`

## V0.2.1

Code now follows PEP8

Fixed somwe variable names in `stats.shufflegroups`

Removed `misc.distancefuncitons`

All distance funcitons are now through `scipy.spatial.distance`

Renamed the argument "do" in `networkmeasures` to "calc".

Renamed the argument "sumOverDim" in `networkmeasures.temporal_degree_centrality` to "axis".

added function `utils.check_distance_funciton_input`

## V0.2.0

Added the module `teneto.derive.derive` with `teneto.derive.postpro_pipeline` which inclues: fisher transform, box cox transform and z transform. Can be configured to which ones are used. 5 methods of deriving temporal networks.

Report generation implemented in derive.

Code made more readable in places.

Added `withinsubnetwork` and `betweensubnetwork` options for volatility.

Optimized `shortest_temporal_path` to dramatically increase speed (was looping the same node multiple times in line 70).

Added the function `utils.multiple_contacts_get_values`

Added possibility to get degree centrality per time point in. `teneto.networkmeasures.temporal_degree_centrality`

Added the ability to specify vmax and vmin in `graphlet_stack_plot`

renamed `clean_subnetwork_indexes` to `clean_community_indexes` (and now included in initializatin)

added warning message to `derive.postpro_boxcox` if one edge fails to be normal.

fixed nLabs/tLabs bug in slice_plot

Added subnetwork option to `temporal_degree_centrality` when do='time''

## V0.1.4 - Released  Feb 2 2017

Changed some types in `rand_binomial` documentation

Added some more customizeable options to `graphlets_stack_plot` (border width, grid color, bordercolor etc.)

Added possibility to call "subnetwork" option in `volatility`

Added function, `clean_subnetwork_indexes` which network index assignment to range between 0 and max(NrSubnetwork)-1.

Updated some of the examples. Also added a ./examples/previous/vx.x.x where previous versions of examples are listed (examples are not created with every new update).

Added (uncommented) the `taxicab_distance` in `misc.distance_functions` option. Won't be added to the documentation of distance functions until I check there is no reason why I commented it. But preliminary testing says it gives the correct answer.

Functions `misc.correct_pvalues_for_multiple_testing` and `misc.corrcoef_matrix` are added but not yet implemented in any of the main functions.

## V0.1.3 - Released Jan 26 2017

Provided clearer documentation in `shortest_temporal_path`

Add possibility of calculating per time point (or per edge/node - but this takes a tone of time) in `volatility`

Added possibility of calculating `temporal_efficiency` per node (either "\_from" to "\_to")

Improved documentation and added references to `rand_binomial`.

## V0.1.2 - Released Jan 6 2017

Fixed bug in `graphlet_stack_plot` which made white colours have black smudges on them. (Also multiple background colours _should_ theoretically be possible now.)

Added option to remove sharpening filter in `graphlet_stack_plot`

Added `misc` and `distance_functions` (fixing `volatility`)

Fixed naming of call to `temporal_shortest_path` in `temporal_efficiency`,`reachability_latency` and `temporal_closeness_centrality`

Added `process_input` function to cut down on repeating code at beginning of networkmeasures

## v0.1.1 - Released Jan 2 2017

### The changes in v0.1.1 make some functions obsolete in v0.1

setup.py has been added for installation (e.g. via pip)

Restructured file structure so that importing teneto has 4 submodules: `plot`, `utils`, `networkmeasures`, `generatenetwork`.

Functions renamed from camel-case to underscore for python-like code.

More comments added to plotting functions

Docs generated and integration with readthedocs.io

Contact representation field `contacts` is now numpy array instead of tuple.

`graphlet_stack_plot` plotting function added.

Examples folder added with several jupyter notebook examples.

Generatenetwork module added. `rand_binomial` function added which generates a random temporal network.

`circle_plot.py` created containing `circle_plot` function (previously in `slice_graph.py`).

variable `vlabs` has been changed to `nlabs`. `dlabs` has been changed to `tlabs`.

Field `nlabs` has been added to contact representation.

`slice_plot` uses information in contact representation when plotting.

scipy dependency now exists (in graphlet_stack_plot).

removed unnecessary and unused import of networkx

restructured the `__init__.py` files for better import of teneto.

## v0.1 - Released Dec 23 2016

Measures, misc, plot, utils folders added.

All measures outlined in From static to temporal network theory paper are added.  (temporal efficiency, closeness centrality, bursty coefficient, reachability latency, intercontactitmes, shortest temporal path, fluctuability, volatility)

Circle_plot and slice_graph added.
