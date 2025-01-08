const {
    Button, TextField, FormControl, InputLabel, Select, MenuItem,
    Typography, Paper, Grid, CircularProgress, Alert, Box, Container
} = MaterialUI;

const root = ReactDOM.createRoot(document.getElementById('root'));

function App() {
    const [formData, setFormData] = React.useState({
        human: {
            role: '',
            hours_worked: '',
            hourly_wage: '',
            task_complexity: 3,
            occupation_code: '',
            is_service_contract: false,
            years_of_service: 0,
            has_eo13706: false,
            contract_date: new Date().toISOString().split('T')[0]
        },
        ai_agent: {
            model: 'GPT-4',
            total_queries: '',
            query_complexity: 3,
            infrastructure_cost: ''
        },
        metrics: {
            collaboration_ratio: 0.7,
            business_value: ''
        }
    });
    
    const [results, setResults] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [error, setError] = React.useState(null);

    const handleChange = (section, field) => (event) => {
        setFormData(prev => ({
            ...prev,
            [section]: {
                ...prev[section],
                [field]: event.target.value
            }
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await fetch('http://localhost:5000/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'Calculation failed');
            }

            setResults(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Container maxWidth="lg">
            <Box sx={{ my: 4 }}>
                <Typography variant="h4" component="h1" gutterBottom align="center">
                    Digital Labor Generator
                </Typography>

                <form onSubmit={handleSubmit}>
                    <Paper sx={{ p: 3, mb: 3 }}>
                        <Typography variant="h5" gutterBottom>
                            Human Employee Information
                        </Typography>
                        <Grid container spacing={3}>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    label="Role"
                                    value={formData.human.role}
                                    onChange={handleChange('human', 'role')}
                                    required
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Hours Worked"
                                    value={formData.human.hours_worked}
                                    onChange={handleChange('human', 'hours_worked')}
                                    required
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Hourly Wage"
                                    value={formData.human.hourly_wage}
                                    onChange={handleChange('human', 'hourly_wage')}
                                    required
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <FormControl fullWidth>
                                    <InputLabel>Task Complexity</InputLabel>
                                    <Select
                                        value={formData.human.task_complexity}
                                        onChange={handleChange('human', 'task_complexity')}
                                        label="Task Complexity"
                                    >
                                        {[1,2,3,4,5].map(num => (
                                            <MenuItem key={num} value={num}>
                                                {num}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    label="Occupation Code"
                                    value={formData.human.occupation_code}
                                    onChange={handleChange('human', 'occupation_code')}
                                    helperText="Enter SCA or Davis-Bacon occupation code"
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <FormControl fullWidth>
                                    <InputLabel>Contract Type</InputLabel>
                                    <Select
                                        value={formData.human.is_service_contract}
                                        onChange={handleChange('human', 'is_service_contract')}
                                        label="Contract Type"
                                    >
                                        <MenuItem value={false}>Davis-Bacon Act</MenuItem>
                                        <MenuItem value={true}>Service Contract Act</MenuItem>
                                    </Select>
                                </FormControl>
                            </Grid>
                        </Grid>
                    </Paper>

                    <Paper sx={{ p: 3, mb: 3 }}>
                        <Typography variant="h5" gutterBottom>
                            AI Agent Information
                        </Typography>
                        <Grid container spacing={3}>
                            <Grid item xs={12} sm={6}>
                                <FormControl fullWidth>
                                    <InputLabel>AI Model</InputLabel>
                                    <Select
                                        value={formData.ai_agent.model}
                                        onChange={handleChange('ai_agent', 'model')}
                                        label="AI Model"
                                    >
                                        <MenuItem value="GPT-4">GPT-4</MenuItem>
                                        <MenuItem value="GPT-3.5">GPT-3.5</MenuItem>
                                        <MenuItem value="Claude">Claude</MenuItem>
                                    </Select>
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Total Queries"
                                    value={formData.ai_agent.total_queries}
                                    onChange={handleChange('ai_agent', 'total_queries')}
                                    required
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <FormControl fullWidth>
                                    <InputLabel>Query Complexity</InputLabel>
                                    <Select
                                        value={formData.ai_agent.query_complexity}
                                        onChange={handleChange('ai_agent', 'query_complexity')}
                                        label="Query Complexity"
                                    >
                                        {[1,2,3,4,5].map(num => (
                                            <MenuItem key={num} value={num}>
                                                {num}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Infrastructure Cost"
                                    value={formData.ai_agent.infrastructure_cost}
                                    onChange={handleChange('ai_agent', 'infrastructure_cost')}
                                    required
                                />
                            </Grid>
                        </Grid>
                    </Paper>

                    <Paper sx={{ p: 3, mb: 3 }}>
                        <Typography variant="h5" gutterBottom>
                            Collaboration Metrics
                        </Typography>
                        <Grid container spacing={3}>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Collaboration Ratio"
                                    value={formData.metrics.collaboration_ratio}
                                    onChange={handleChange('metrics', 'collaboration_ratio')}
                                    inputProps={{ step: 0.1, min: 0, max: 1 }}
                                    required
                                    helperText="Value between 0 and 1"
                                />
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <TextField
                                    fullWidth
                                    type="number"
                                    label="Business Value"
                                    value={formData.metrics.business_value}
                                    onChange={handleChange('metrics', 'business_value')}
                                    required
                                />
                            </Grid>
                        </Grid>
                    </Paper>

                    <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}>
                        <Button
                            variant="contained"
                            color="primary"
                            type="submit"
                            disabled={loading}
                            size="large"
                        >
                            {loading ? <CircularProgress size={24} /> : 'Calculate'}
                        </Button>
                    </Box>
                </form>

                {error && (
                    <Alert severity="error" sx={{ mb: 3 }}>
                        {error}
                    </Alert>
                )}

                {results && (
                    <Paper sx={{ p: 3 }}>
                        <Typography variant="h5" gutterBottom>
                            Results
                        </Typography>
                        <Grid container spacing={3}>
                            <Grid item xs={12} md={6}>
                                <Paper sx={{ p: 2 }}>
                                    <Typography variant="h6">Human Wages</Typography>
                                    <Typography>Base Pay: ${results.human_wages.base_pay.toFixed(2)}</Typography>
                                    <Typography>Health & Welfare: ${results.human_wages.health_welfare?.toFixed(2) || 0}</Typography>
                                    <Typography>Vacation Pay: ${results.human_wages.vacation_pay?.toFixed(2) || 0}</Typography>
                                    <Typography>Holiday Pay: ${results.human_wages.holiday_pay?.toFixed(2) || 0}</Typography>
                                    <Typography variant="subtitle1" sx={{ mt: 1 }}>
                                        Total: ${results.human_wages.total_compensation.toFixed(2)}
                                    </Typography>
                                </Paper>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <Paper sx={{ p: 2 }}>
                                    <Typography variant="h6">AI Costs</Typography>
                                    <Typography>Total: ${results.ai_costs.toFixed(2)}</Typography>
                                </Paper>
                            </Grid>
                            <Grid item xs={12}>
                                <Paper sx={{ p: 2 }}>
                                    <Typography variant="h6">Recommendations</Typography>
                                    <Typography>Action: {results.wage_recommendations.action}</Typography>
                                    <Typography>Adjustment: {results.wage_recommendations.adjustment_percentage}%</Typography>
                                    <Typography>Reason: {results.wage_recommendations.reason}</Typography>
                                </Paper>
                            </Grid>
                        </Grid>
                    </Paper>
                )}
            </Box>
        </Container>
    );
}

root.render(<App />);
